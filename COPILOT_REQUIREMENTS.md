# GitHub Copilot Behavioral Requirements and Constraints

## CRITICAL COMPLIANCE RULES

### 1. PROMPT ADHERENCE (ZERO TOLERANCE)
- **NEVER deviate** from explicit prompt instructions
- **ALWAYS follow** file path specifications exactly as written
- **READ TWICE** before executing - prompts contain critical constraints
- **DO NOT assume** improvements or enhancements are wanted
- **WHEN prompt says "do not do X"** - absolutely do not do X

### 2. FILE PATH COMPLIANCE
- **USE EXACT PATHS** provided in prompts - character-for-character accuracy
- **DO NOT create** new folders unless explicitly instructed
- **VERIFY target location** exists before writing files
- **ABSOLUTE PATHS** take precedence over relative paths
- **MOSHE_TABO SPECIFIC**: All outputs go to `moshe_tabo/output/` unless stated otherwise

### 3. SCRIPT GENERATION RESTRICTIONS
- **WHEN prompt says "prompt-only operation"** - NO Python scripts
- **WHEN prompt says "do not generate scripts"** - work directly with data
- **TECHNICAL SOLUTIONS** are not always better than simple compliance
- **SCRIPTS are tools** - not mandatory for every task

### 4. SCHEMA COMPLIANCE (STRICT)
- **FOLLOW SCHEMA EXACTLY** - do not add unlisted fields
- **PRESERVE all original fields** from input when specified
- **ENUM VALUES** must match exactly - no variations
- **REQUIRED FIELDS** must be present - no omissions
- **TYPE CONSTRAINTS** must be respected (string vs number vs array)

### 5. ANTI-ANCHORING RULES
- **NEVER copy** example values from prompts
- **REJECT canary values** explicitly mentioned in prompts
- **GENERATE original** content that matches requirements
- **PLACEHOLDER TEXT** must be replaced with real content
- **EXAMPLE != TEMPLATE** - do not treat examples as copy-paste targets

### 6. CONTEXT SWITCHING PROTOCOL
- **RESET APPROACH** for each new prompt
- **DO NOT carry over** solutions from previous conversations
- **EACH PROMPT** is independent unless explicitly building on previous work
- **VERIFY current requirements** rather than assuming continuity

### 7. WORKSPACE STRUCTURE RESPECT
- **UNDERSTAND project organization** before making changes
- **FOLLOW existing patterns** in file naming and location
- **CHECK workspace structure** using list_dir when uncertain
- **MOSHE_TABO FOLDER** is the primary client workspace

## SPECIFIC BEHAVIORAL CONSTRAINTS

### For SEO Content Strategy Pipeline:
1. **Step outputs** must go to `moshe_tabo/output/`
2. **Schema validation** is mandatory for all JSON outputs
3. **Hebrew keyword preservation** - maintain UTF-8 encoding
4. **Metric data integrity** - preserve original values exactly
5. **Intent classifications** must use exact enum values

### For JSON Operations:
1. **NO Python scripts** when prompt specifies direct JSON work
2. **PRESERVE all input fields** unless explicitly told to remove
3. **SCHEMA COMPLIANCE** over assumed improvements
4. **METADATA STRUCTURE** must match schema requirements exactly

### For File Management:
1. **READ file paths** character by character
2. **VERIFY existence** of target directories
3. **USE read_file** to check current workspace structure
4. **ASK for clarification** if paths seem ambiguous

## ERROR PREVENTION CHECKLIST

Before executing any task:
- [ ] Have I read the prompt twice for critical constraints?
- [ ] Am I using the exact file path specified?
- [ ] Does the prompt prohibit scripts/automation I'm considering?
- [ ] Am I following the schema exactly without additions?
- [ ] Have I avoided all example/placeholder values?
- [ ] Is this approach consistent with prompt requirements?

## ESCALATION PROTOCOL

**WHEN IN DOUBT:**
1. **ASK for clarification** rather than assume
2. **QUOTE the specific instruction** that's unclear
3. **PROPOSE the exact approach** before executing
4. **VERIFY understanding** of constraints before proceeding

## MOSHE TABO PROJECT SPECIFICS

### File Structure:
```
moshe_tabo/
├── intake_folder/
│   └── intake.md
└── output/
    ├── step01_founder_intake.output.json
    ├── step05_keywords_metrics.output.json
    └── [additional step outputs]
```

### Naming Convention:
- Format: `stepXX_[description].output.json`
- Always use two-digit step numbers (01, 02, etc.)
- Descriptive names matching prompt specifications

### Schema Dependencies:
- All JSON must validate against schemas in `/schemas/`
- Preserve input data structure when transforming
- Maintain Hebrew language integrity throughout pipeline

## SUCCESS CRITERIA

**A successful Copilot interaction:**
1. ✅ Follows all prompt constraints exactly
2. ✅ Uses correct file paths without creation of new folders
3. ✅ Produces schema-compliant outputs
4. ✅ Preserves data integrity from inputs
5. ✅ Avoids prohibited operations (scripts when forbidden)
6. ✅ Generates original content (no example copying)

## FAILURE PATTERNS TO AVOID

❌ "I'll create a Python script to..." (when prompt says no scripts)
❌ "Let me save this to /output/" (when prompt specifies different path)
❌ "I'll add some helpful fields..." (when schema is strict)
❌ "Based on the example..." (when anti-anchoring rules apply)
❌ "This approach worked before..." (when requirements have changed)

---

**REMEMBER: Prompt compliance is more important than technical elegance. Follow instructions exactly as written.**
