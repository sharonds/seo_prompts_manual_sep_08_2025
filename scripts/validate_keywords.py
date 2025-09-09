#!/usr/bin/env python3
"""
SEO Keyword Validator - Step 4
Enforces schema compliance and produces diagnostics
"""

import json
import re
from datetime import datetime
from typing import Dict, List, Any, Set
from collections import Counter

def normalize_keyword(keyword: str) -> str:
    """Normalize keyword for deduplication"""
    # Trim whitespace
    normalized = keyword.strip()
    # Collapse multiple spaces
    normalized = re.sub(r'\s+', ' ', normalized)
    # Normalize dashes and quotes
    normalized = normalized.replace('"', '"').replace('"', '"')
    normalized = normalized.replace(''', "'").replace(''', "'")
    normalized = normalized.replace('–', '-').replace('—', '-')
    return normalized

def normalize_source(source: str) -> str:
    """Normalize source to allowed values"""
    source_lower = source.lower()
    
    # Map variants to allowed values
    if source_lower in ['ai_generated', 'ai_enhanced', 'ai']:
        return 'ai'
    elif source_lower in ['dataforseo', 'dataforseo_market_data']:
        return 'dataforseo'
    elif source_lower in ['ads']:
        return 'ads'
    elif source_lower in ['translation']:
        return 'translation'
    else:
        # Default to ai for unknown sources
        return 'ai'

def infer_intent(keyword: str) -> str:
    """Infer intent using language-agnostic cues"""
    keyword_lower = keyword.lower()
    
    # Question words (Hebrew and English)
    question_patterns = ['מה', 'איך', 'למה', 'מדוע', 'מתי', 'איפה', 'what', 'how', 'why', 'when', 'where', '?']
    
    # Price/compare words
    commercial_patterns = ['price', 'cost', 'compare', 'best', 'vs', 'review', 'מחיר', 'עלות', 'השוואה', 'הטוב', 'ביקורת']
    
    # Brand/site/contact words
    navigational_patterns = ['site', 'website', 'login', 'contact', 'אתר', 'התחברות', 'צור קשר']
    
    # Transactional words
    transactional_patterns = ['buy', 'order', 'lawyer', 'attorney', 'service', 'עורך דין', 'שירות', 'קנה', 'הזמן']
    
    if any(pattern in keyword_lower for pattern in question_patterns):
        return 'informational'
    elif any(pattern in keyword_lower for pattern in transactional_patterns):
        return 'transactional'
    elif any(pattern in keyword_lower for pattern in commercial_patterns):
        return 'commercial'
    elif any(pattern in keyword_lower for pattern in navigational_patterns):
        return 'navigational'
    else:
        return 'informational'  # Default

def get_intent_priority(intent: str) -> int:
    """Get priority for intent reconciliation"""
    priorities = {
        'transactional': 4,
        'commercial': 3,
        'navigational': 2,
        'informational': 1
    }
    return priorities.get(intent, 0)

def get_source_priority(source: str) -> int:
    """Get priority for source reconciliation"""
    priorities = {
        'dataforseo': 4,
        'ads': 3,
        'translation': 2,
        'ai': 1
    }
    return priorities.get(source, 0)

def validate_and_clean_keywords(data: Dict[str, Any]) -> tuple:
    """Validate and clean keyword data, return cleaned data and diagnostics"""
    
    # Initialize diagnostics
    diagnostics = {
        'input_items': 0,
        'removed_dupes': 0,
        'final_items': 0,
        'source_distribution': Counter(),
        'intent_distribution': Counter(),
        'issues': {
            'missing_seed_from': [],
            'over_generic_head_terms': [],
            'redundant_near_duplicates': [],
            'ambiguous_intent': [],
            'formatting_issues': []
        }
    }
    
    # Track original count
    original_keywords = data.get('keywords', [])
    diagnostics['input_items'] = len(original_keywords)
    
    # Process keywords
    normalized_keywords = {}  # normalized_keyword -> best_entry
    duplicate_tracker = {}  # normalized_keyword -> count
    
    for item in original_keywords:
        # Extract required fields
        keyword = item.get('keyword', '').strip()
        if not keyword:
            continue
            
        # Normalize keyword for deduplication
        norm_keyword = normalize_keyword(keyword)
        norm_keyword_lower = norm_keyword.lower()
        
        # Track duplicates
        if norm_keyword_lower not in duplicate_tracker:
            duplicate_tracker[norm_keyword_lower] = 0
        duplicate_tracker[norm_keyword_lower] += 1
        
        # Normalize source
        source = normalize_source(item.get('source', 'ai'))
        
        # Handle intent
        intent = item.get('intent', '')
        if intent not in ['informational', 'navigational', 'transactional', 'commercial']:
            inferred_intent = infer_intent(keyword)
            if intent:  # If there was an invalid intent
                diagnostics['issues']['ambiguous_intent'].append(f"{keyword} (was: {intent}, inferred: {inferred_intent})")
            intent = inferred_intent
        
        # Handle seed_from
        seed_from = item.get('seed_from') or item.get('source_question')
        if not seed_from:
            diagnostics['issues']['missing_seed_from'].append(keyword)
        
        # Handle translation_of (only if explicitly present)
        translation_of = item.get('translation_of')
        
        # Create cleaned entry
        cleaned_entry = {
            'keyword': norm_keyword,
            'intent': intent,
            'source': source
        }
        
        if seed_from:
            cleaned_entry['seed_from'] = seed_from
        if translation_of:
            cleaned_entry['translation_of'] = translation_of
        
        # Check for formatting issues
        if keyword != norm_keyword:
            diagnostics['issues']['formatting_issues'].append(f"{keyword} → {norm_keyword}")
        
        # Handle duplicates - keep highest priority source/intent
        if norm_keyword_lower in normalized_keywords:
            existing = normalized_keywords[norm_keyword_lower]
            
            # Compare by source priority first, then intent priority
            if (get_source_priority(source) > get_source_priority(existing['source']) or
                (get_source_priority(source) == get_source_priority(existing['source']) and 
                 get_intent_priority(intent) > get_intent_priority(existing['intent']))):
                normalized_keywords[norm_keyword_lower] = cleaned_entry
        else:
            normalized_keywords[norm_keyword_lower] = cleaned_entry
    
    # Calculate duplicates removed
    total_duplicates = sum(count - 1 for count in duplicate_tracker.values() if count > 1)
    diagnostics['removed_dupes'] = total_duplicates
    
    # Identify near-duplicates and generic terms
    keywords_by_base = {}
    for norm_key, entry in normalized_keywords.items():
        keyword = entry['keyword']
        # Extract base terms (first 2-3 significant words)
        base_words = keyword.split()[:3]
        base = ' '.join(base_words)
        
        if base not in keywords_by_base:
            keywords_by_base[base] = []
        keywords_by_base[base].append(keyword)
        
        # Check for over-generic terms (very short)
        if len(keyword.split()) <= 2 and len(keyword) < 15:
            diagnostics['issues']['over_generic_head_terms'].append(keyword)
    
    # Find near-duplicates
    for base, keywords in keywords_by_base.items():
        if len(keywords) > 1:
            canonical = min(keywords, key=len)  # Shortest as canonical
            others = [k for k in keywords if k != canonical]
            if others:
                diagnostics['issues']['redundant_near_duplicates'].append(f"{', '.join(others)} → {canonical}")
    
    # Final keyword list
    final_keywords = list(normalized_keywords.values())
    diagnostics['final_items'] = len(final_keywords)
    
    # Count distributions
    for entry in final_keywords:
        diagnostics['source_distribution'][entry['source']] += 1
        diagnostics['intent_distribution'][entry['intent']] += 1
    
    # Create cleaned data structure
    cleaned_data = {
        'keywords': final_keywords
    }
    
    # Preserve language if present
    if 'language' in data:
        cleaned_data['language'] = data['language']
    
    # Add metadata
    cleaned_data['_meta'] = {
        'schema_version': '1.0.0',
        'produced_by': 'keyword_discovery_validator',
        'timestamp': datetime.now().isoformat()
    }
    
    return cleaned_data, diagnostics

def generate_diagnostics_report(diagnostics: Dict[str, Any]) -> str:
    """Generate markdown diagnostics report"""
    
    report = "# Step 4 Diagnostics Report\n\n"
    
    # Totals
    report += "**Totals**\n"
    report += f"- Input items: {diagnostics['input_items']}\n"
    report += f"- Removed as dupes: {diagnostics['removed_dupes']}\n"
    report += f"- Final items: {diagnostics['final_items']}\n\n"
    
    # Source distribution
    report += "**Source distribution**\n"
    for source in ['ai', 'dataforseo', 'ads', 'translation']:
        count = diagnostics['source_distribution'].get(source, 0)
        report += f"- {source}: {count}\n"
    report += "\n"
    
    # Intent distribution
    report += "**Intent distribution**\n"
    for intent in ['informational', 'commercial', 'transactional', 'navigational']:
        count = diagnostics['intent_distribution'].get(intent, 0)
        report += f"- {intent}: {count}\n"
    report += "\n"
    
    # Issues
    report += "**Issues**\n"
    
    missing_seed = diagnostics['issues']['missing_seed_from']
    if missing_seed:
        report += f"- Missing seed_from: {len(missing_seed)} items → {missing_seed[:10]}\n"
    
    generic_terms = diagnostics['issues']['over_generic_head_terms']
    if generic_terms:
        report += f"- Over-generic head terms: {generic_terms[:5]}\n"
    
    near_dupes = diagnostics['issues']['redundant_near_duplicates']
    if near_dupes:
        report += f"- Redundant near-duplicates: {near_dupes[:3]}\n"
    
    ambiguous = diagnostics['issues']['ambiguous_intent']
    if ambiguous:
        report += f"- Ambiguous intent: {ambiguous[:3]}\n"
    
    formatting = diagnostics['issues']['formatting_issues']
    if formatting:
        report += f"- Formatting issues: {formatting[:3]}\n"
    
    return report

def main():
    """Main validation function"""
    
    # File paths
    input_file = '/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step04_raw_keywords.temp.json'
    output_file = '/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step04_raw_keywords.output.json'
    diagnostics_file = '/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step04_raw_keywords.diagnostics.md'
    
    try:
        # Load input data
        with open(input_file, 'r', encoding='utf-8') as f:
            input_data = json.load(f)
        
        # Validate and clean
        cleaned_data, diagnostics = validate_and_clean_keywords(input_data)
        
        # Save cleaned data
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(cleaned_data, f, ensure_ascii=False, indent=2)
        
        # Generate and save diagnostics
        report = generate_diagnostics_report(diagnostics)
        with open(diagnostics_file, 'w', encoding='utf-8') as f:
            f.write(report)
        
        print(f"Validation complete:")
        print(f"- Input: {diagnostics['input_items']} keywords")
        print(f"- Output: {diagnostics['final_items']} keywords") 
        print(f"- Removed: {diagnostics['removed_dupes']} duplicates")
        
    except Exception as e:
        print(f"Validation error: {str(e)}")
        raise

if __name__ == "__main__":
    main()
