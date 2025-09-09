# Copilot Instructions for SEO Content Strategy Pipeline

## 🧠 Big Picture Architecture

This is a **manual recipe engine** for generating SEO content strategies through a 7-step pipeline. Each step transforms JSON data through AI prompts, with strict schema validation between steps.

**Core Components:**
- `/prompts/` - AI role-based instructions (1_founder_intake.md → 7_content_strategy.md)
- `/schemas/` - JSON Schema contracts defining data flow between steps
- `/moshe_tabo/output/` - Client workspace with `stepXX_name.output.json` files
- `COPILOT_REQUIREMENTS.md` - Critical behavioral constraints (READ FIRST)

## 🔄 Pipeline Data Flow

```
Founder Intake → Business Profile → ICP → Journey → Keywords → Metrics → Clusters → Strategy
```

Each step depends on the previous step's output JSON. The pipeline supports Hebrew/English markets with DataForSEO integration for keyword metrics.

## ⚠️ Critical Execution Rules

**ALWAYS READ `COPILOT_REQUIREMENTS.md` FIRST** - Contains zero-tolerance compliance rules.

### File Path Protocol
- Client outputs: `moshe_tabo/output/stepXX_description.output.json`
- Never deviate from specified paths - exact character matching required
- Use `list_dir` to verify workspace structure before file operations

### Schema Compliance
- Every JSON must validate against its corresponding schema in `/schemas/`
- Preserve all required fields, respect enum values exactly
- Include `_meta` object with schema_version, produced_by, timestamp

### Prompt Execution
- Each prompt in `/prompts/` defines role, task, input/output schema
- Follow instructions literally - no "improvements" or assumptions
- When prompt says "do not generate scripts" - work directly with data

## 🛠️ Development Workflows

### Running a Pipeline Step
1. Read the prompt file (e.g., `prompts/4_keyword_discovery.md`)
2. Verify input JSON exists and matches expected schema
3. Execute prompt instructions exactly as written
4. Validate output against schema before saving
5. Save to correct client folder with proper naming convention

### Schema Evolution
- Schemas use semantic versioning (v1.1, v1.2)
- Always evolve additively - never remove/rename fields in minor versions
- Update schema references in prompts when versions change

### Hebrew Language Handling
- Preserve UTF-8 encoding for Hebrew keywords
- Market context: Israeli insurance/healthcare sectors
- Integration with DataForSEO for Hebrew search metrics

## 🔧 Key Integration Points

### DataForSEO MCP Integration
- Step 5 (keyword metrics) uses DataForSEO API for search volume/difficulty
- Fallback to AI estimates when API data unavailable
- Hebrew market focus requires proper language/location parameters

### External Data Sources
- Google Ads XML reports in `moshe_tabo/GAW_data/`
- Manual intake files in `moshe_tabo/intake_folder/`

## 📁 File Organization Patterns

```
/client_name/
  ├── intake_folder/          # Initial business context
  ├── output/                 # Pipeline step outputs
  └── GAW_data/              # Google Ads export data
```

**Naming Convention:** `stepXX_description.output.json` (e.g., `step01_founder_intake.output.json`)

## 🎯 Project-Specific Conventions

- **Recipe Engine Philosophy:** Prompts are flexible, schemas are stable contracts
- **End-to-Start Design:** Final content strategy drives backward requirements
- **Manual Mode:** No automation layer - each step run individually in VS Code
- **Quality over Speed:** Schema compliance and Hebrew language preservation prioritized
- **Traceability:** Every output includes provenance metadata for debugging

## 🚨 Common Pitfalls to Avoid

1. **Path Deviation:** Saving outputs to wrong directories (use exact paths from prompts)
2. **Schema Violations:** Adding unauthorized fields or wrong data types
3. **Script Generation:** Creating Python scripts when prompts specify manual-only operations
4. **Context Anchoring:** Copying example values instead of generating original content
5. **UTF-8 Issues:** Breaking Hebrew character encoding in keyword processing
