#!/usr/bin/env python3
"""
Keywords Merger Script - Step 4c
Merges Google Ads Search Terms XML export with existing raw keywords JSON
"""

import xml.etree.ElementTree as ET
import json
import re
from datetime import datetime
from typing import List, Dict, Any

def extract_keywords_from_xml(xml_file_path: str) -> List[Dict[str, Any]]:
    """Extract keywords from Google Ads XML export"""
    
    # Parse the XML file
    tree = ET.parse(xml_file_path)
    root = tree.getroot()
    
    keywords = []
    
    # Find all row elements in the XML
    for row in root.findall('.//row'):
        keyword_text = None
        clicks = 0
        impressions = 0
        
        # Extract keyword and performance data
        for cell in row.findall('cell'):
            key_elem = cell.find('key')
            value_elem = cell.find('value')
            
            if key_elem is not None and value_elem is not None:
                key = key_elem.text
                value = value_elem.text
                
                if key == 'Search keyword':
                    keyword_text = value
                elif key == 'Clicks':
                    try:
                        clicks = int(value) if value else 0
                    except ValueError:
                        clicks = 0
                elif key == 'Impr.':
                    try:
                        impressions = int(value) if value else 0
                    except ValueError:
                        impressions = 0
        
        # Only include keywords with actual text and some performance
        if keyword_text and keyword_text.strip():
            # Determine intent based on keyword characteristics
            intent = determine_intent(keyword_text)
            
            keywords.append({
                "keyword": keyword_text.strip(),
                "intent": intent,
                "source": "ads",
                "seed_from": "google_ads_campaign"
            })
    
    return keywords

def determine_intent(keyword: str) -> str:
    """Determine search intent based on keyword characteristics"""
    keyword_lower = keyword.lower()
    
    # Transactional indicators in Hebrew
    transactional_patterns = [
        'עורך דין', 'משרד עורכי דין', 'יעוץ משפטי', 'ייעוץ', 'טלפון', 'פגישה',
        'עלות', 'מחיר', 'תשלום', 'זול', 'יקר', 'הצעת מחיר'
    ]
    
    # Commercial investigation indicators
    commercial_patterns = [
        'השוואה', 'מומלץ', 'הטוב ביותר', 'ביקורות', 'המלצות', 'דירוג',
        'אילו', 'איך לבחור', 'מה עדיף'
    ]
    
    # Informational indicators
    informational_patterns = [
        'מה זה', 'איך', 'למה', 'מדוע', 'מתי', 'איפה', 'מידע', 'הסבר',
        'הגדרה', 'מדריך', 'טיפים', 'זכויות', 'תהליך', 'חוק'
    ]
    
    # Navigational indicators (looking for specific entities)
    navigational_patterns = [
        'ביטוח לאומי', 'משרד הבריאות', 'מוסד', 'ממשלה', 'רשות',
        'אתר', 'דף', 'פורטל'
    ]
    
    # Check patterns in order of specificity
    if any(pattern in keyword_lower for pattern in transactional_patterns):
        return 'transactional'
    elif any(pattern in keyword_lower for pattern in commercial_patterns):
        return 'commercial'
    elif any(pattern in keyword_lower for pattern in navigational_patterns):
        return 'navigational'
    elif any(pattern in keyword_lower for pattern in informational_patterns):
        return 'informational'
    else:
        # Default classification based on keyword structure
        if 'עורך דין' in keyword_lower or 'משרד' in keyword_lower:
            return 'transactional'
        elif '?' in keyword or keyword_lower.startswith(('מה', 'איך', 'למה', 'מתי')):
            return 'informational'
        else:
            return 'commercial'

def load_existing_keywords(json_file_path: str) -> Dict[str, Any]:
    """Load existing keywords JSON file"""
    with open(json_file_path, 'r', encoding='utf-8') as f:
        return json.load(f)

def merge_keywords(existing_data: Dict[str, Any], ads_keywords: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Merge Google Ads keywords with existing keywords, avoiding duplicates"""
    
    # Create a set of existing keywords for duplicate checking
    existing_keywords_set = {kw['keyword'].lower() for kw in existing_data['keywords']}
    
    # Filter out duplicates from ads keywords
    new_keywords = []
    for kw in ads_keywords:
        if kw['keyword'].lower() not in existing_keywords_set:
            new_keywords.append(kw)
            existing_keywords_set.add(kw['keyword'].lower())
    
    # Merge the keywords
    merged_data = existing_data.copy()
    merged_data['keywords'] = existing_data['keywords'] + new_keywords
    
    # Update metadata
    merged_data['_meta']['timestamp'] = datetime.now().isoformat()
    merged_data['_meta']['produced_by'] = 'keyword_discovery_merged_ads'
    
    return merged_data

def main():
    """Main execution function"""
    
    # File paths
    xml_file = '/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/GAW_data/Search_keyword_report.xml'
    json_file = '/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step04_raw_keywords.output.json'
    output_file = '/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step04_raw_keywords_merged.output.json'
    
    try:
        # Extract keywords from Google Ads XML
        print("Extracting keywords from Google Ads XML...")
        ads_keywords = extract_keywords_from_xml(xml_file)
        print(f"Found {len(ads_keywords)} keywords from Google Ads")
        
        # Load existing keywords
        print("Loading existing keywords...")
        existing_data = load_existing_keywords(json_file)
        print(f"Found {len(existing_data['keywords'])} existing keywords")
        
        # Merge keywords
        print("Merging keywords...")
        merged_data = merge_keywords(existing_data, ads_keywords)
        
        # Count new keywords added
        new_count = len(merged_data['keywords']) - len(existing_data['keywords'])
        print(f"Added {new_count} new keywords from Google Ads")
        print(f"Total keywords after merge: {len(merged_data['keywords'])}")
        
        # Save merged data
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(merged_data, f, ensure_ascii=False, indent=2)
        
        print(f"Merged keywords saved to: {output_file}")
        
        # Print sample of new keywords
        if new_count > 0:
            print("\nSample of new keywords added:")
            sample_new = ads_keywords[:min(5, len(ads_keywords))]
            for kw in sample_new:
                if kw['keyword'].lower() not in {k['keyword'].lower() for k in existing_data['keywords']}:
                    print(f"  - {kw['keyword']} ({kw['intent']})")
    
    except Exception as e:
        print(f"Error during merge: {str(e)}")
        raise

if __name__ == "__main__":
    main()
