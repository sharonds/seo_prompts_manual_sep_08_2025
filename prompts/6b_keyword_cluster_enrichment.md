# Step 6B — Cluster Enrichment (v1.1)

## Role
You are an **SEO Strategist**.

## Goal
Enrich raw clusters from Step 6A with priority, reasoning, and recommended content type. Output must conform exactly to `keyword_clusters.schema.json`.

## Inputs
1. Raw clusters JSON (Step 6A):  
   `/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step06_clusters_raw.output.json`

2. Step 5 metrics JSON (read-only for context):  
   `/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step05_keywords_metrics.output.json`

## Task
1. **Pass-through**: Copy clusters + keyword objects verbatim from Step 6A.  
2. **Dominant intent**: Ensure each cluster has one. If missing, compute as mode of `intent` (tie-breaker: highest `search_volume`, treating `"unknown"` as 0).  
3. **Recommended content type**: Assign one of: `blog`, `FAQ`, `guide`, `landing page`.  
   - Informational → blog/guide  
   - Navigational → FAQ/landing page  
   - Transactional → landing page  
   - Commercial → guide/landing page  
4. **Priority**: Assign `high`, `medium`, `low` with simple heuristics.  
   - High: ≥2 keywords with `search_volume` ≥500 or strong buying intent terms  
   - Medium: mixed intents or mid-range volume (200–1000)  
   - Low: mostly unknown volume, informational intent only  
5. **Priority reasoning**: 1–2 sentences. Reference volumes/intents briefly.

## Output
JSON only. Must validate against `/schemas/keyword_clusters.schema.json` (v1.1).  

- Save to:  
  `/Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step06_keyword_clusters.output.json`

## Meta
- `_meta.schema_version` = `"1.1.0"`  
- `_meta.produced_by` = `"keyword_clustering"`  
- `_meta.timestamp` = current ISO 8601 UTC