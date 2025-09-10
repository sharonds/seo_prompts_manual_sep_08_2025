# EXECUTE PROMPT (Step 5 — Keyword Metrics Enrichment)

READ FIRST:
- Use the prompt file (do not summarize it):  
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/prompts/5_keyword_metrics.md
- Follow this schema exactly (no extra fields):  
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/schemas/keywords_with_metrics.schema.json

EXECUTION CONSTRAINTS:
- Prompt-only. Do NOT create or run Python scripts.
- Output JSON only (no prose).
- Preserve all Step 4 fields per keyword (`source`, `seed_from`, `translation_of`).
- Add metrics fields only from schema:  
  `search_volume`, `difficulty`, `cpc`, `metrics_source`, `cpc_currency`, `metrics_last_updated`.
- Use sourcing precedence: DataForSEO > Ads > AI estimate > Unknown.
- Normalize values: `"unknown"` for missing metrics, lowercase enums.

SAVE & FORMAT:
- Save to (ensure folder exists first):  
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step05_keywords_with_metrics.output.json
- UTF-8, Unix newlines, 2-space indentation.

VALIDATION BEFORE SAVE:
1. Validate against keywords_with_metrics.schema.json (v1.2).
2. Top-level keys only: `keywords`, `_meta`.
3. Ensure all keyword objects contain at minimum: `keyword`, `intent`.
4. Ensure `metrics_source` values ∈ {dataforseo, ads, ai_estimate, unknown}.
5. Ensure numeric fields are numbers where known; `"unknown"` string otherwise.

FINAL CHECK (reply exactly):
COMPLIANCE VERIFIED — JSON saved, schema-valid, no scripts.