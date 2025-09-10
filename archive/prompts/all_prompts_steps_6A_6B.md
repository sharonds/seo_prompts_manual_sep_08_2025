# All Prompts: Steps 6A and 6B

## Step 6A: Keyword Clustering (Raw, v1.0)

# Step 6A — Keyword Clustering (Raw, v1.0)

## Role
You are an SEO Strategist.

## Goal
Cluster keywords by semantic similarity and shared intent to streamline content planning. Preserve keyword objects exactly as provided by Step 5.

## Critical Rules
- ALWAYS read `COPILOT_REQUIREMENTS.md` first (File Path Protocol, Schema Compliance, UTF-8 preservation for Hebrew).
- Do NOT generate scripts; work directly with data.
- Schema compliance is mandatory; no extra fields beyond schema at the top level.
- Preserve all keyword fields exactly (names, values, types). Do not fabricate or mutate values.

## Input
File:
`/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step05_keywords_metrics.output.json`

- The input is a JSON object produced in Step 5 that conforms to `/schemas/keywords_with_metrics.schema.json`.
- Use the `keywords` array from that object as the input list to cluster.
- Each keyword object may include (non-exhaustive):
  - `keyword`
  - `intent`
  - `search_volume` (integer or "unknown")
  - `difficulty` (number or "unknown")
  - `cpc` (number or "unknown")
  - `metrics_source` ("ads" | "dataforseo" | "ai_estimate" | "unknown")
  - Optional: `cpc_currency`, `metrics_last_updated` (ISO 8601 date-time), `source`, `seed_from`, `translation_of`, and any other pass-through fields from Step 5

## Task
1) Clustering
- Group keywords into clusters by semantic similarity and shared intent.
- Each cluster must include:
  - `cluster_name`: short, descriptive, unique theme label
  - `dominant_intent`: mode of intents in the cluster; tie-breaker = highest total `search_volume` (treat "unknown" as 0). If computing this would require mutating any keyword, set `dominant_intent` to the most common non-null `intent` value among the cluster as-is.
  - `keywords`: list of preserved keyword objects (no changes, no additions)

2) Sizing and consolidation (adaptive)
- If 0 keywords: return `"clusters": []` and stop.
- If 1–2 keywords: create a single cluster named `"General"`.
- If 3–23 keywords: create `ceil(n/5)` clusters, target 3–10 keywords per cluster.
- If ≥24 keywords: aim for 8–12 clusters, target 3–10 keywords per cluster.
- If any cluster ends with <3 keywords after initial pass, merge it into the closest semantic cluster.
- If cluster count >12, iteratively merge the most similar until ≤12 remain.

## Output
Return JSON only. Must conform to `raw_clusters.schema.json`.

- Save to:  
  `/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step06_clusters_raw.output.json`

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
        "required": ["cluster_name", "keywords"]
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

## Meta
- `_meta.schema_version` = `"1.1.0-raw"`
- `_meta.produced_by` = `"keyword_clustering_raw"`
- `_meta.timestamp` = current ISO 8601 UTC (e.g., `2025-09-10T13:15:00Z`)

## Language
- Preserve UTF-8 Hebrew text exactly as in input.

## Step 6B: Cluster Enrichment (v1.1)

# Step 6B — Cluster Enrichment (v1.1)

## Role
You are an SEO Strategist.

## Goal
Enrich raw clusters from Step 6A with priority and recommended content type, producing a final output that conforms exactly to `/schemas/keyword_clusters.schema.json` (v1.1).

## Critical Rules
- ALWAYS read `COPILOT_REQUIREMENTS.md` first (File Path Protocol, Schema Compliance, UTF-8 preservation for Hebrew).
- Do NOT generate scripts; work directly with data.
- Schema compliance is mandatory; use field names and enums exactly as defined in `schemas/keyword_clusters.schema.json`.
- Do not add or remove fields from keyword objects; pass them through unchanged from the raw clusters.

## Inputs
1) Raw clusters JSON from Step 6A:
`/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step06_clusters_raw.output.json`

2) Step 5 metrics JSON (read-only for context, do not override Step 6A keyword objects):
`/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step05_keywords_metrics.output.json`

## Task
Produce the final clusters by:
1) Pass-through: Copy clusters and keyword objects from Step 6A verbatim.
2) dominant_intent: If empty or missing in a cluster, compute as the most common `intent` within that cluster (tie-breaker by highest total `search_volume`, treating "unknown" as 0). If still ambiguous, omit `dominant_intent`.
3) recommended_content_type: Set one of: "blog", "FAQ", "landing page", "guide" based on cluster intent and query types.
   - Informational clusters → blog or guide
   - Navigational → FAQ or landing page depending on brand patterns
   - Transactional → landing page
   - Commercial → guide or landing page
4) priority: Assign "high", "medium", or "low". Use a simple heuristic:
   - High: clusters with ≥2 keywords having `search_volume` ≥ 500 or containing strong buying keywords (e.g., includes price/quote/cost/insurance company).
   - Medium: clusters with aggregate `search_volume` between 200–1000, or mixed intents.
   - Low: clusters with very low or unknown volumes and purely informational intent.
5) priority_reasoning: 1–2 sentences explaining the choice; reference volumes and intent briefly. Keep it concise and non-marketing.

## Output
JSON only (no prose). Must validate against `/schemas/keyword_clusters.schema.json` (v1.1).
- Save to: `/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step06_keyword_clusters.output.json`
- Include `_meta` with:
  - `schema_version`: "1.1.0"
  - `produced_by`: "keyword_clustering"
  - `timestamp`: ISO 8601 UTC

## Validation Checklist
- Top-level keys: `clusters`, `_meta` only.
- For each cluster:
  - Required: `cluster_name`, `keywords`.
  - Optional: `dominant_intent`, `recommended_content_type`, `priority`, `priority_reasoning`.
  - No extra fields.
- For each keyword object:
  - Do not modify field names or values.
  - Ensure `metrics_source` is one of: `ads`, `dataforseo`, `ai_estimate`, `unknown`. If it isn’t, set it to `"unknown"` in the output only if necessary to pass schema, but prefer preserving as-is when valid.

## Language
- Preserve UTF-8 Hebrew text exactly as in input.

## Step 6 Schema

The final output for Step 6 must conform to the following JSON schema:

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
```
