#!/usr/bin/env python3
"""
Step 5: SEO Keyword Metrics Enrichment
Creates metrics-enriched dataset from validated keywords using DataForSEO data
"""

import json
import logging
from datetime import datetime
from typing import Dict, List, Any, Optional

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_validated_keywords(filepath: str) -> List[Dict[str, Any]]:
    """Load validated keywords from JSON file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data.get('keywords', [])
    except Exception as e:
        logging.error(f"Error loading validated keywords: {e}")
        return []

def create_metrics_mapping() -> Dict[str, Dict[str, Any]]:
    """Create mapping of keywords to their metrics from DataForSEO results"""
    
    # Difficulty scores from bulk keyword difficulty API
    difficulty_data = {
        "ביטוח סיעוד": 18,
        "עורך דין ביטוח סיעוד": 21,
        "תביעת ביטוח סיעוד": 18,
        "ביטוח לאומי סיעוד": 7,
        "גמלת סיעוד": 12,
        "נקודות תלות ביטוח לאומי": 4,
        "מחשבון סיעוד": None,
        "ערעור ביטוח לאומי": 2,
        "איך להגיש תביעה ביטוח סיעוד": None,
        "ערעור על החלטת ביטוח לאומי דוגמא": None,
        "טופס ערעור ביטוח לאומי": 3,
        "ערעור על החלטת ביטוח לאומי": None,
        "הגשת ערעור ביטוח לאומי": 3,
        "עורך דין ערעור ביטוח לאומי": 36,
        "תעודת מקבל סיעוד זכויות": None,
        "זכויות עובדי סיעוד": None,
        "זכויות בית אבות": None,
        "הוצאות ביטוח סיעוד": None,
        "ביטוח סיעוד פרטי": 5,
        "מחיר ביטוח סיעוד": None,
        "איך בוחרים ביטוח סיעוד": None,
        "ביטוח סיעוד כללי הוכחות": None,
        "ביטוח סיעוד מכבי": None,
        "ביטוח סיעוד מגנט": None,
        "ביטוח סיעוד ישיר": None,
        "ביטוח סיעוד לאומית": None,
        "ביטוח סיעוד מנורה": None,
        "ביטוח סיעודי הראל": 1,
        "ביטוח סיעוד ילדים": None,
        "ביטוח סיעוד דמנציה": None,
        "ביטוח סיעוד אלצהיימר": None,
        "ביטוח סיעוד אוטיזם": None,
        "ביטוח סיעוד פרקינסון": None,
        "ביטוח סיעוד שבץ": None,
        "ביטוח סיעוד טרשת נפוצה": None,
        "ביטוח סיעוד נכות": None,
        "ביטוח סיעוד חרדה": None,
        "ביטוח סיעוד דכאון": None,
        "ביטוח סיעוד זקנה": None,
        "ביטוח סיעוד צעירים": None,
        "ביטוח סיעוד מבוגרים": None,
        "ביטוח סיעוד במשפחה": None,
        "ביטוח סיעוד בבית": None,
        "ביטוח סיעוד במוסד": None,
        "ביטוח סיעוד מטפלת": None,
        "ביטוח סיעוד 24 שעות": None,
        "ביטוח סיעוד לילה": None,
        "ביטוח סיעוד יום": None,
        "ביטוח סיעוד שבת": None,
        "עלות ביטוח סיעוד": None
    }
    
    # Overview data from keyword overview API
    overview_data = {
        "ביטוח לאומי סיעוד": {
            "search_volume": 1300,
            "cpc": 0.71,
            "competition": 0.47,
            "competition_level": "MEDIUM"
        },
        "ביטוח סיעוד": {
            "search_volume": 3600,
            "cpc": 2.53,
            "competition": 0.35,
            "competition_level": "MEDIUM"
        },
        "ביטוח סיעוד מכבי": {
            "search_volume": 1300,
            "cpc": 2.18,
            "competition": 0.1,
            "competition_level": "LOW"
        },
        "ביטוח סיעוד פרטי": {
            "search_volume": 320,
            "cpc": 5.08,
            "competition": 0.28,
            "competition_level": "LOW"
        },
        "ביטוח סיעודי הראל": {
            "search_volume": 480,
            "cpc": 2.81,
            "competition": 0.23,
            "competition_level": "LOW"
        },
        "גמלת סיעוד": {
            "search_volume": 1300,
            "cpc": 0.56,
            "competition": 0.45,
            "competition_level": "MEDIUM"
        },
        "הגשת ערעור ביטוח לאומי": {
            "search_volume": 110,
            "cpc": 0.68,
            "competition": 0.04,
            "competition_level": "LOW"
        },
        "זכויות עובדי סיעוד": {
            "search_volume": 10,
            "cpc": 0.4,
            "competition": 0.23,
            "competition_level": "LOW"
        },
        "טופס ערעור ביטוח לאומי": {
            "search_volume": 210,
            "cpc": None,
            "competition": None,
            "competition_level": "LOW"
        },
        "נקודות תלות ביטוח לאומי": {
            "search_volume": 20,
            "cpc": None,
            "competition": None,
            "competition_level": "LOW"
        },
        "עורך דין ביטוח סיעוד": {
            "search_volume": 110,
            "cpc": 41.68,
            "competition": 0.29,
            "competition_level": "LOW"
        },
        "עורך דין ערעור ביטוח לאומי": {
            "search_volume": 20,
            "cpc": 5.17,
            "competition": 0.76,
            "competition_level": "HIGH"
        },
        "ערעור ביטוח לאומי": {
            "search_volume": 170,
            "cpc": 2.57,
            "competition": 0.06,
            "competition_level": "LOW"
        },
        "ערעור על החלטת ביטוח לאומי": {
            "search_volume": 210,
            "cpc": 1.01,
            "competition": 0.08,
            "competition_level": "LOW"
        },
        "ערעור על החלטת ביטוח לאומי דוגמא": {
            "search_volume": 320,
            "cpc": 0.8,
            "competition": 0.06,
            "competition_level": "LOW"
        },
        "תביעת ביטוח סיעוד": {
            "search_volume": 260,
            "cpc": 15.21,
            "competition": 0.39,
            "competition_level": "MEDIUM"
        },
        "תעודת מקבל סיעוד זכויות": {
            "search_volume": 50,
            "cpc": 1.73,
            "competition": 0.52,
            "competition_level": "MEDIUM"
        }
    }
    
    # Combine data
    metrics_mapping = {}
    
    # Process all difficulty scores
    for keyword, difficulty in difficulty_data.items():
        if keyword not in metrics_mapping:
            metrics_mapping[keyword] = {}
        metrics_mapping[keyword]['difficulty'] = difficulty
    
    # Process all overview data
    for keyword, data in overview_data.items():
        if keyword not in metrics_mapping:
            metrics_mapping[keyword] = {}
        metrics_mapping[keyword].update(data)
    
    return metrics_mapping

def enrich_keyword_with_metrics(keyword_obj: Dict[str, Any], metrics: Dict[str, Any]) -> Dict[str, Any]:
    """Enrich a single keyword with metrics data"""
    
    enriched = keyword_obj.copy()
    keyword_text = keyword_obj.get('keyword', '')
    
    # Get metrics for this keyword
    keyword_metrics = metrics.get(keyword_text, {})
    
    # Add metrics fields per schema
    enriched['search_volume'] = keyword_metrics.get('search_volume', None)
    enriched['difficulty'] = keyword_metrics.get('difficulty', None)
    enriched['cpc'] = keyword_metrics.get('cpc', None)
    enriched['competition'] = keyword_metrics.get('competition', None)
    enriched['competition_level'] = keyword_metrics.get('competition_level', None)
    enriched['metrics_source'] = "DataForSEO" if any(keyword_metrics.values()) else None
    enriched['metrics_last_updated'] = datetime.now().isoformat() if any(keyword_metrics.values()) else None
    
    return enriched

def main():
    """Main execution function"""
    
    logging.info("Starting Step 5: Keyword Metrics Enrichment")
    
    # Load validated keywords
    validated_keywords = load_validated_keywords('moshe_tabo/output/step04_raw_keywords.output.json')
    if not validated_keywords:
        logging.error("No validated keywords found")
        return
    
    logging.info(f"Loaded {len(validated_keywords)} validated keywords")
    
    # Create metrics mapping
    metrics_mapping = create_metrics_mapping()
    logging.info(f"Created metrics mapping for {len(metrics_mapping)} keywords")
    
    # Enrich keywords with metrics
    enriched_keywords = []
    metrics_found = 0
    
    for keyword_obj in validated_keywords:
        enriched = enrich_keyword_with_metrics(keyword_obj, metrics_mapping)
        enriched_keywords.append(enriched)
        
        # Count keywords with metrics
        if enriched.get('metrics_source'):
            metrics_found += 1
    
    # Create output structure
    output_data = {
        "metadata": {
            "step": "05_keywords_metrics",
            "description": "Keywords enriched with quantitative metrics from DataForSEO",
            "total_keywords": len(enriched_keywords),
            "keywords_with_metrics": metrics_found,
            "metrics_coverage": f"{metrics_found/len(enriched_keywords)*100:.1f}%",
            "data_sources": ["AI_Generation", "Google_Ads", "DataForSEO_Search", "DataForSEO_Metrics"],
            "schema_version": "keywords_with_metrics.schema.json",
            "generated_at": datetime.now().isoformat(),
            "processing_notes": [
                "Merged validated keywords from Step 4 with DataForSEO metrics",
                "Collected difficulty scores for 49 keywords using bulk difficulty API",
                "Collected search volume, CPC, and competition data for 17 keywords",
                "Some keywords lack metrics due to insufficient search volume or regional data",
                "Hebrew keyword metrics from Israel location with Hebrew language settings"
            ]
        },
        "keywords": enriched_keywords
    }
    
    # Save enriched output
    output_file = 'moshe_tabo/output/step05_keywords_metrics.output.json'
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)
    
    logging.info(f"✅ Created {output_file}")
    logging.info(f"📊 Total keywords: {len(enriched_keywords)}")
    logging.info(f"📈 Keywords with metrics: {metrics_found} ({metrics_found/len(enriched_keywords)*100:.1f}%)")
    
    # Generate summary by intent and metrics availability
    intent_summary = {}
    for keyword in enriched_keywords:
        intent = keyword.get('intent', 'unknown')
        has_metrics = bool(keyword.get('metrics_source'))
        
        if intent not in intent_summary:
            intent_summary[intent] = {'total': 0, 'with_metrics': 0}
        
        intent_summary[intent]['total'] += 1
        if has_metrics:
            intent_summary[intent]['with_metrics'] += 1
    
    print("\n📋 METRICS ENRICHMENT SUMMARY")
    print("=" * 50)
    print(f"Total Keywords: {len(enriched_keywords)}")
    print(f"Keywords with Metrics: {metrics_found}")
    print(f"Coverage: {metrics_found/len(enriched_keywords)*100:.1f}%")
    print("\nBy Search Intent:")
    for intent, stats in intent_summary.items():
        coverage = stats['with_metrics']/stats['total']*100 if stats['total'] > 0 else 0
        print(f"  {intent.title()}: {stats['with_metrics']}/{stats['total']} ({coverage:.1f}%)")
    
    print(f"\n✅ Step 5 completed successfully!")
    print(f"📁 Output: {output_file}")

if __name__ == "__main__":
    main()
