# EXECUTE PROMPT (Step 6 — Keyword Clustering)

READ FIRST:
- Use the prompt file (do not summarize it):  
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/prompts/6_keyword_clustering.md
- Input from Step 5:  
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step05_keywords_metrics.output.json
- Follow this schema exactly (no extra fields):  
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/schemas/keyword_clusters.schema.json

EXECUTION CONSTRAINTS:
- Prompt-only. Do NOT create or run Python scripts.  
- Output JSON only (no prose).  
- Do not copy placeholder/example values.  
- Preserve all Step 5 fields per keyword when present:
  source, seed_from, translation_of, cpc_currency, metrics_last_updated.
- Aim for TOTAL 8–12 clusters; each cluster has ~3–10 keywords.
- Group keywords into clusters based on semantic similarity and shared intent.  

SAVE & FORMAT:
- Save to (ensure folder exists first):  
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step06_keyword_clusters.output.json  
- UTF-8, Unix newlines, 2-space indentation.  

VALIDATION BEFORE SAVE:
1. Validate against keyword_clusters.schema.json.  
2. Confirm **only** top-level keys: `clusters`, `_meta`.  
3. Ensure every cluster has `cluster_name` and `keywords`.  
4. Check each keyword preserves Step 5 fields:  
   - `keyword`, `intent`, `search_volume`, `difficulty`, `cpc`,  
   - `metrics_source`, `cpc_currency`, `metrics_last_updated`,  
   - `source`, `seed_from`, `translation_of`.  
5. Report any detected issues or suggested improvements in a dedicated diagnostics block.  
6. No properties outside the schema.  

FINAL CHECK (reply exactly):  
COMPLIANCE VERIFIED — JSON saved, schema-valid, no scripts.