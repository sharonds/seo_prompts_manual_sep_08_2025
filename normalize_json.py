#!/usr/bin/env python3
"""
JSON Normalizer for Step 5 Keywords Metrics
Transforms the current output to strictly match keywords_with_metrics.schema.json
"""

import json
import yaml
from datetime import datetime
from typing import Dict, Any, List

def load_current_json(filepath: str) -> Dict[str, Any]:
    """Load the current JSON file"""
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def normalize_metrics_source(source: str) -> str:
    """Normalize metrics_source to schema enum values"""
    if not source:
        return "unknown"
    
    source_lower = source.lower()
    if source_lower == "dataforseo":
        return "dataforseo"
    elif source_lower == "ads":
        return "ads"
    elif source_lower == "ai_estimate":
        return "ai_estimate"
    else:
        return "unknown"

def normalize_keyword(keyword_obj: Dict[str, Any]) -> Dict[str, Any]:
    """Transform a keyword object to match schema exactly"""
    
    # Start with only whitelisted fields
    normalized = {
        "keyword": keyword_obj.get("keyword", ""),
        "intent": keyword_obj.get("intent", "informational")
    }
    
    # Handle search_volume
    search_volume = keyword_obj.get("search_volume")
    if search_volume is None:
        normalized["search_volume"] = "unknown"
    elif isinstance(search_volume, (int, float)):
        normalized["search_volume"] = int(search_volume)
    else:
        normalized["search_volume"] = "unknown"
    
    # Handle difficulty
    difficulty = keyword_obj.get("difficulty")
    if difficulty is None:
        normalized["difficulty"] = "unknown"
    elif isinstance(difficulty, (int, float)):
        normalized["difficulty"] = float(difficulty)
    else:
        normalized["difficulty"] = "unknown"
    
    # Handle cpc
    cpc = keyword_obj.get("cpc")
    if cpc is None:
        normalized["cpc"] = "unknown"
    elif isinstance(cpc, (int, float)):
        normalized["cpc"] = float(cpc)
    else:
        normalized["cpc"] = "unknown"
    
    # Handle metrics_source
    metrics_source = keyword_obj.get("metrics_source", "")
    normalized["metrics_source"] = normalize_metrics_source(metrics_source)
    
    return normalized

def create_meta() -> Dict[str, Any]:
    """Create the _meta object according to schema"""
    return {
        "schema_version": "1.0.0",
        "produced_by": "keyword_metrics",
        "timestamp": datetime.now().isoformat()
    }

def analyze_coverage(keywords: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Analyze metrics coverage for diagnostics"""
    
    total_keywords = len(keywords)
    keywords_with_any_metric = 0
    keywords_with_full_metrics = 0
    metrics_source_counts = {"ads": 0, "dataforseo": 0, "ai_estimate": 0, "unknown": 0}
    
    for keyword in keywords:
        has_any_metric = False
        has_full_metrics = True
        
        # Check if has any metrics
        if (keyword.get("search_volume") != "unknown" or 
            keyword.get("difficulty") != "unknown" or 
            keyword.get("cpc") != "unknown"):
            has_any_metric = True
            keywords_with_any_metric += 1
        
        # Check if has full metrics
        if (keyword.get("search_volume") == "unknown" or 
            keyword.get("difficulty") == "unknown" or 
            keyword.get("cpc") == "unknown"):
            has_full_metrics = False
        
        if has_full_metrics and has_any_metric:
            keywords_with_full_metrics += 1
        
        # Count metrics sources
        source = keyword.get("metrics_source", "unknown")
        if source in metrics_source_counts:
            metrics_source_counts[source] += 1
    
    return {
        "total_keywords": total_keywords,
        "keywords_with_any_metric": keywords_with_any_metric,
        "keywords_with_full_metrics": keywords_with_full_metrics,
        "by_metrics_source": metrics_source_counts,
        "coverage_percentage": round(keywords_with_any_metric / total_keywords * 100, 1) if total_keywords > 0 else 0,
        "full_metrics_percentage": round(keywords_with_full_metrics / total_keywords * 100, 1) if total_keywords > 0 else 0
    }

def main():
    """Main transformation function"""
    
    input_file = "/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step05_keywords_metrics.output.json"
    coverage_file = "/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/_step05_metrics_coverage.yaml"
    
    # Load current JSON
    current_data = load_current_json(input_file)
    
    # Transform keywords
    normalized_keywords = []
    dropped_fields = set()
    
    for keyword_obj in current_data.get("keywords", []):
        # Track dropped fields
        for field in keyword_obj:
            if field not in ["keyword", "intent", "search_volume", "difficulty", "cpc", "metrics_source"]:
                dropped_fields.add(field)
        
        # Normalize keyword
        normalized = normalize_keyword(keyword_obj)
        normalized_keywords.append(normalized)
    
    # Create schema-compliant output
    schema_compliant = {
        "keywords": normalized_keywords,
        "_meta": create_meta()
    }
    
    # Analyze coverage for diagnostics
    coverage_analysis = analyze_coverage(normalized_keywords)
    coverage_analysis["dropped_fields"] = sorted(list(dropped_fields))
    coverage_analysis["transformation_notes"] = [
        "Transformed from original step05 output to strict schema compliance",
        "Moved 'metadata' to '_meta' with required fields",
        "Removed non-schema fields: " + ", ".join(sorted(dropped_fields)),
        "Normalized 'DataForSEO' → 'dataforseo' in metrics_source",
        "Converted null values to 'unknown' strings",
        "Preserved all keyword text and intent classifications"
    ]
    
    # Write normalized JSON
    with open(input_file, 'w', encoding='utf-8') as f:
        json.dump(schema_compliant, f, ensure_ascii=False, indent=2)
    
    # Write coverage diagnostics
    with open(coverage_file, 'w', encoding='utf-8') as f:
        yaml.dump(coverage_analysis, f, default_flow_style=False, allow_unicode=True)
    
    print(f"✅ Normalized JSON written to: {input_file}")
    print(f"📊 Coverage analysis written to: {coverage_file}")
    print(f"📈 Keywords with metrics: {coverage_analysis['keywords_with_any_metric']}/{coverage_analysis['total_keywords']} ({coverage_analysis['coverage_percentage']}%)")
    print(f"🔧 Dropped fields: {', '.join(dropped_fields)}")

if __name__ == "__main__":
    main()
