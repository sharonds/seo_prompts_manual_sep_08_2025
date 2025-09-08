Great idea 🙌 — having a Prompt Design Guide will give you (and Copilot) a repeatable way to build and refine prompts for every step. Here’s a version you can save in /docs/prompt_design_guide.md:

⸻

🧩 Prompt Design Guide (Foundation SEO Recipe)

This guide explains how to build prompts for each step in the recipe. Prompts are the brains of the workflow — they connect inputs (schemas) to outputs (schemas) using the business logic.

⸻

1. Prompt Structure (Template)

Every prompt follows the same sections:

# Prompt Template

## Role
You are [role], responsible for [task].

## Input
You are given JSON input conforming to schema: [input schema file/path].

## Task
- Analyze the provided input.
- Apply the step’s business logic.
- Respect dependencies (see dependency map).
- If data is missing, output `"unknown"` instead of hallucinating.

## Output
Produce JSON strictly conforming to schema: [output schema file/path].

- Validate against required fields.
- Include `_meta` with:
  - `schema_version`
  - `produced_by`
  - `timestamp`
- Do not add extra fields not in schema.


⸻

2. Design Principles
	•	Schema Awareness
Always include both the input schema (what the AI can rely on) and the output schema (what it must produce).
	•	Role Clarity
Assign the AI a clear role (e.g., “Market Researcher,” “SEO Strategist”).
	•	Determinism > Creativity
For Foundation phase, favor precision and structure over creative flourishes.
Use phrasing like: “Do not invent data; if unavailable, write ‘unknown’.”
	•	Traceability
Ensure _meta is always filled with:
	•	schema_version (e.g., 1.0.0)
	•	produced_by (step name, e.g., icp_definition)
	•	timestamp (ISO date-time)

⸻

3. Step-Specific Adjustments
	•	Founder Intake → ICP
Map industry → persona context, services → needs, goals → persona goals.
	•	ICP → Customer Journey
Use pains → questions, goals → content_needs, behaviors → funnel mapping.
	•	Customer Journey → Keywords
Expand questions + content_needs into raw keyword ideas.
	•	Keywords → Metrics
Enrich keywords with search volume, difficulty, CPC. If no data, mark "unknown".
	•	Metrics → Clusters
Group keywords into semantic clusters, assign dominant intent, and priority.
	•	Clusters → Content Plan
Translate clusters into pillars, funnel stages, and actionable content ideas.

⸻

4. Testing Prompts
	1.	Unit test each prompt with a minimal JSON input → check if output matches schema.
	2.	Chain test: run two steps in sequence to validate dependencies (e.g., Intake → ICP → Journey).
	3.	Edge case test: missing data, niche markets, Hebrew keywords. Ensure "unknown" works.

⸻

👉 With this guide, you can build and refine each prompt consistently, without “forgetting” the constraints that keep the workflow robust.

