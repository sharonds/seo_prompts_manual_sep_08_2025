# EXECUTE PROMPT (Step 4 — Keyword Discovery)

READ FIRST:
- Use the prompt file (do not summarize it): 
  /.../prompts/4_keyword_discovery.md
- Follow this schema exactly (no extra fields):
  /.../schemas/raw_keywords.schema.json

EXECUTION CONSTRAINTS:
- Prompt-only. Do NOT create or run Python scripts.
- Output JSON only (no prose).
- Do not include metrics (search_volume, cpc, difficulty) in Step 4.

SAVE & FORMAT:
- Save to:
  /.../output/step04_raw_keywords.temp.json
- UTF-8, Unix newlines, 2-space indentation.

VALIDATION BEFORE SAVE:
1) Validate against raw_keywords.schema.json.
2) Top-level keys only: "language", "keywords", "_meta".
3) Each keyword has keyword, intent, source, seed_from (and translation_of only when a translation occurred).
4) No properties outside the schema.

FINAL CHECK (reply exactly):
COMPLIANCE VERIFIED — JSON saved, schema-valid, no scripts.