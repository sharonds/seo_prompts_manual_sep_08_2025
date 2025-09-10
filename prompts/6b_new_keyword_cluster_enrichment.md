# Step 6B — Cluster Enrichment (v1.2)

## Role  
You are an **SEO Strategist**.

## Goal  
Enrich raw clusters from Step 6A with:  
- `dominant_intent`  
- `recommended_content_type`  
- `priority`  
- `priority_reasoning`  

The output must conform exactly to the schema below (`keyword_clusters.schema.json`, v1.1).

---

## Inputs  
1. Raw clusters JSON (Step 6A):  
   `/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step06_clusters_raw.output.json`  

2. Step 5 metrics JSON (read-only, do not override Step 6A fields):  
   `/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step05_keywords_metrics.output.json`  

---

## Task  

1. **Pass-through**  
   - Copy clusters and keyword objects verbatim from Step 6A.  
   - Do not add, remove, or rename fields inside keyword objects.  
   - Only add fields required by this step (`recommended_content_type`, `priority`, `priority_reasoning`).  

2. **Dominant intent**  
   - Each cluster must have `dominant_intent`.  
   - Compute as the most common `intent` among keywords.  
   - Tie-breaker 1: highest total `search_volume` (treat `"unknown"` as 0).  
   - Tie-breaker 2: fallback to schema order: `informational` → `navigational` → `transactional` → `commercial`.  

3. **Recommended content type**  
   - Choose one of: `blog`, `FAQ`, `guide`, `landing page`.  
   - Heuristic:  
     - Informational → blog or guide  
     - Navigational → FAQ or landing page  
     - Transactional → landing page  
     - Commercial → guide or landing page  

4. **Priority**  
   - Assign: `high`, `medium`, or `low`.  
   - Use a simple heuristic:  
     - High → ≥2 keywords with `search_volume` ≥ 500 OR clear buying intent terms (lawyer, price, company).  
     - Medium → aggregate `search_volume` 200–1000 OR mix of intents with some commercial terms.  
     - Low → mostly `"unknown"` search volumes with informational-only intent.  

5. **Priority reasoning**  
   - Add 1–2 sentences explaining why the priority was chosen.  
   - Reference volumes, CPC, or clear buying intent if available.  
   - Keep concise and factual.  

---

## Output  
- JSON only (no prose).  
- Must validate against the schema below.  
- Save to:  
  `/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step06_keyword_clusters.output.json`  

---

### Final Schema (v1.1)  

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Keyword Clusters (Foundation) — v1.1",
  "type": "object",
  "properties": {
    "clusters": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "cluster_name": { "type": "string" },
          "dominant_intent": {
            "type": "string",
            "enum": ["informational", "navigational", "transactional", "commercial"]
          },
          "keywords": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "keyword": { "type": "string" },
                "search_volume": { "type": ["integer", "string"] },
                "difficulty": { "type": ["number", "string"] },
                "cpc": { "type": ["number", "string"] },
                "metrics_source": {
                  "type": "string",
                  "enum": ["ads", "dataforseo", "ai_estimate", "unknown"]
                },
                "cpc_currency": { "type": "string" },
                "metrics_last_updated": { "type": "string", "format": "date-time" },
                "intent": {
                  "type": "string",
                  "enum": ["informational", "navigational", "transactional", "commercial"]
                },
                "source": { "type": "string", "enum": ["ads", "dataforseo", "ai", "translation"] },
                "seed_from": { "type": "string" },
                "translation_of": { "type": "string" }
              },
              "required": ["keyword"]
            }
          },
          "recommended_content_type": { "type": "string", "description": "blog, FAQ, landing page, guide" },
          "priority": { "type": "string", "enum": ["high", "medium", "low"] },
          "priority_reasoning": { "type": "string" }
        },
        "required": ["cluster_name", "keywords"]
      }
    },
    "_meta": {
      "type": "object",
      "properties": {
        "schema_version": { "type": "string", "default": "1.1.0" },
        "produced_by": { "type": "string", "default": "keyword_clustering" },
        "timestamp": { "type": "string", "format": "date-time" }
      },
      "required": ["schema_version", "produced_by", "timestamp"]
    }
  },
  "required": ["clusters", "_meta"],
  "additionalProperties": false
}```