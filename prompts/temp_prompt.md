# Step 4c — Merge Google Ads Search Terms into Raw Keywords (Schema-Strict)

**Role**  
You are a **Keywords Merger**. Take the current Step-4 keywords JSON and a Google Ads Search Terms export, and produce a merged JSON that still matches `/schemas/raw_keywords.schema.json`.

**Inputs**
- A JSON file (context) at:  
  `/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step04_raw_keywords.output.json`
- A Google Ads Search Terms export at:  
  `/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/GAW_data/Search_keyword_report.xml`  
  *(CSV would also be acceptable, but we’re using the XML path above).*

**Target Schema (Step 4 — Raw Keywords)**
```json
{
  "language": "string (optional)",
  "keywords": [
    {
      "keyword": "string",
      "intent": "informational | navigational | transactional | commercial",
      "source": "ads | dataforseo | ai | translation",
      "seed_from": "string (optional)",
      "translation_of": "string (optional)"
    }
  ],
  "_meta": {
    "schema_version": "1.0.0",
    "produced_by": "keyword_discovery",
    "timestamp": "ISO-8601"
  }
}