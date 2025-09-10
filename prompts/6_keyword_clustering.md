# Step 6 — Keyword Clustering (Foundation, v2.1)

## Role  
You are an **SEO Strategist**.

## Goal  
Organize enriched keywords into meaningful clusters based on semantic similarity and shared intent.  
This will streamline content planning and improve topical authority.

## Input  
File:  
`/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step05_keywords_metrics.output.json`

- JSON array of keyword records.  
- Each record may contain:  
  - `keyword`  
  - `intent`  
  - `search_volume` (integer or `"unknown"`)  
  - `difficulty` (number or `"unknown"`)  
  - `cpc` (number or `"unknown"`)  
  - `metrics_source`  
  - Optional fields (if present): `cpc_currency`, `metrics_last_updated`, `source`, `seed_from`, `translation_of`  
- **Preserve every field exactly as provided.**  
- All numeric values must remain numeric where known; use `"unknown"` only if data is missing.

## Task  
1. **Clustering**  
   - Group keywords into clusters by semantic similarity and shared intent.  
   - Each cluster must include:  
     - `cluster_name` (short descriptive theme)  
     - `keywords` (list of preserved keyword objects)  
     - `dominant_intent` = mode of intents in the cluster.  
       - If tied, select the intent with the **highest total search volume** (treat `"unknown"` as 0).  
   - Constraints:  
     - **8–12 clusters** total.  
     - **3–10 keywords per cluster**.  
     - If a cluster has <3 keywords, merge it into the closest semantic cluster.  
     - If clusters exceed 12, iteratively merge the most similar until ≤12 remain.  

2. **Priority Scoring**  
   - Assign `priority`: `high` | `medium` | `low`.  
   - Justify in `priority_reasoning`.  
   - Keep logic simple; advanced weighting will be applied later.

3. **Content Type Recommendation**  
   - Add `recommended_content_type`: one of `blog`, `FAQ`, `guide`, `landing page`.  

## Output  
Return JSON only (no prose). Must conform exactly to the schema below.

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
}