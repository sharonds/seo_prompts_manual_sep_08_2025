# EXECUTE PROMPT (Step 2 — ICP Definition)

READ FIRST:
- Use the prompt file (do not summarize it):  
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/prompts/2_icp_definition.md
- Follow this schema exactly (no extra fields):  
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/schemas/icp.schema.json

EXECUTION CONSTRAINTS:
- Prompt-only. Do NOT create or run Python scripts.
- Output JSON only (no prose).
- Generate **2–3 personas** as specified in the logic prompt.
- Ensure each persona includes all required fields:
  persona_name, description, context, pains, goals, behaviors.

SAVE & FORMAT:
- Save to:  
  /Users/sharonsciammas/seo_prompts_manual_sep_08_2025/output/step02_icp_definition.output.json
- UTF-8, Unix newlines, 2-space indentation.

VALIDATION BEFORE SAVE:
1) Validate against icp.schema.json.
2) Top-level keys only: "personas", "_meta".
3) Ensure all required persona fields are present and arrays are non-empty.
4) Ensure _meta includes schema_version, produced_by, timestamp.
5) No properties outside the schema.

FINAL CHECK (reply exactly):  
COMPLIANCE VERIFIED — JSON saved, schema-valid, no scripts.