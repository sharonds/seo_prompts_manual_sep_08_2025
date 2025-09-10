# EXECUTE PROMPT (Step 7 — Foundational Content Plan)

READ FIRST:
- Use the prompt file (do not summarize it):  
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/prompts/7_content_strategy.md
- Input from Step 6:
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step06_keyword_clusters.output.json
- Follow this schema exactly (no extra fields):  
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/schemas/content_strategy.schema.json

EXECUTION CONSTRAINTS:
- Prompt-only. Do NOT create or run Python scripts.  
- Output JSON only (no prose).  
- Transform keyword clusters into content pillars with specific content ideas.
- Preserve all cluster fields from Step 6, including keyword metrics, when embedding clusters into pillars.  
- Each cluster must be assigned to exactly one pillar.  
- Total 3–5 pillars; total 10–15 content ideas across all pillars.  

SAVE & FORMAT:
- Save to (ensure folder exists first):  
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/moshe_tabo/output/step07_content_strategy.output.json  
- UTF-8, Unix newlines, 2-space indentation.  

VALIDATION BEFORE SAVE:
1. Validate against content_strategy.schema.json.  
2. Ensure proper transformation from keyword clusters to content pillars.
3. Verify all required schema fields are present.
4. Confirm Hebrew content is properly encoded.
5. No properties outside the schema.  

FINAL CHECK (reply exactly):  
COMPLIANCE VERIFIED — JSON saved, schema-valid, no scripts.