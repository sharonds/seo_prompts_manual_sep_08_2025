# Step 6A — Keyword Clustering (Raw, v1.1)

## Role
You are an **SEO Strategist**.

## Goal
Group enriched keywords from Step 5 into raw clusters by semantic similarity and shared intent. Preserve all keyword objects exactly as provided.

## Input
File:  
`/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step05_keywords_metrics.output.json`

- JSON object conforming to `/schemas/keywords_with_metrics.schema.json`.  
- Use the `keywords` array as the input list.  
- Preserve every field exactly (`keyword`, `intent`, `search_volume`, etc.). No modifications, no new fields.

## Task
Follow rules in this strict order: 1) Schema compliance, 2) Preserve fields, 3) Semantic grouping.

1. **Clustering**
   - Group keywords into clusters by semantic similarity + intent.  
   - Each cluster must include:
     - `cluster_name`: short, descriptive label  
     - `keywords`: list of preserved keyword objects (unchanged)  
       Each keyword must appear in exactly one cluster (no duplicates).  
   - Include dominant_intent: mode of intents in the cluster. If tied, select the most frequent intent. If still tied, select by highest total search_volume (treat "unknown" as 0).

2. **Sizing**
   - 0 keywords → return `"clusters": []`.  
   - 1–2 keywords → single `"General"` cluster.  
   - 3–23 keywords → create ceil(n/5) clusters. Each cluster must contain 3–10 keywords (strict).  
   - ≥24 keywords → create 8–12 clusters. Each cluster must contain 3–10 keywords (strict).  
   - No cluster may exceed 10 keywords.  
   - If <3 keywords remain in a cluster → merge with nearest semantic cluster.  
   - If >12 clusters → iteratively merge until ≤12.  

## Output
Return JSON only. Must conform to `raw_clusters.schema.json`.

- Save to:  
  `/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step06_clusters_raw.output.json`

Never output null. If a value is missing, use "unknown" or omit the field if optional.

### Raw Clusters Schema
```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Keyword Clusters (Raw) — v1.1",
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
            "items": { "type": "object", "required": ["keyword"], "additionalProperties": true }
          }
        },
        "required": ["cluster_name", "keywords", "dominant_intent"]
      }
    },
    "_meta": {
      "type": "object",
      "properties": {
        "schema_version": { "type": "string", "const": "1.1.0-raw" },
        "produced_by": { "type": "string", "const": "keyword_clustering_raw" },
        "timestamp": { "type": "string", "format": "date-time" }
      },
      "required": ["schema_version", "produced_by", "timestamp"]
    }
  },
  "required": ["clusters", "_meta"]
}
```