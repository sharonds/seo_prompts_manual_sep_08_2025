Manual Design Guide — Recipe Engine (MVP)

1. Core Idea

This system is a recipe engine:
	•	Prompts = instructions (Role / Task / Goal).
	•	Schemas = contracts between steps.
	•	Runners = small scripts or tool calls.
	•	Orchestrator = runs the recipe (YAML flow).
	•	Recipes = ordered steps that create business artifacts (e.g. SEO Content Strategy).

The philosophy: keep prompts flexible, keep schemas stable.

⸻

2. Design Principles
	1.	Contracts First
	•	Schemas define required fields → downstream steps rely on them.
	•	Always evolve schemas additively (never remove/rename fields in minor versions).
	2.	End-to-Start Design
	•	Freeze the final output contract (TOC) first (e.g. content_strategy).
	•	Work backwards to see what each step must provide.
	3.	Prompts as Iterative Layer
	•	Prompts can evolve endlessly as long as they respect schema contracts.
	•	Use prompt fragments (evidence, specificity, strict JSON) to increase quality.
	4.	Traceability
	•	Every schema includes metadata:

"_meta": {
  "schema_name": "string",
  "schema_version": "x.y.z",
  "produced_by": "step_name",
  "provenance": ["ai","tool"],
  "timestamp": "ISO-8601"
}


	5.	Schema Levels
	•	Required = downstream breaks without it.
	•	Preferred = improves quality; evaluator can penalize if missing.
	•	Optional = future-proof fields.

⸻

3. Design Flow

Step A — Define Business Logic
	•	Write high-level flow: steps, goals, roles, tasks.
	•	Example (SEO):
	1.	Founder Intake → Business Profile
	2.	ICP Definition
	3.	Customer Journey
	4.	Keyword Discovery
	5.	Keyword Metrics
	6.	Keyword Clustering
	7.	Content Strategy

Step B — Final Output Contract (TOC)
	•	Define the final schema (e.g. content_strategy.schema.v1.json).
	•	Include fields like pillars, funnel_stage, clusters.
	•	This schema anchors the whole pipeline.

Step C — Dependency Map
	•	Write a one-page mapping of where each field comes from. Example:

content_strategy.pillars[].clusters[] ← keyword_clusters.clusters[]
keyword_clusters.clusters[]           ← keywords_with_metrics.keywords[]
keywords_with_metrics.keywords[]      ← raw_keywords.keywords[]
raw_keywords.intent                   ← customer_journey.stages[].content_needs
customer_journey.stages[]             ← icp.personas[].pains/goals
icp.personas[]                        ← business_profile.value_props/segments



Step D — Step Specs, business logic (Text Only)
	•	For each step:
	•	Role
	•	Goal
	•	Task
	•	Inputs Required
	•	Outputs Promised

Step E — Extract Schemas
	•	Convert Inputs Required + Outputs Promised → JSON schemas.
	•	Tag fields as Required / Preferred / Optional.

Step F — Write Prompts
	•	Draft prompts that produce the schema-defined outputs.
	•	Add clauses for evidence, specificity, and strict JSON.

⸻

4. Recipe YAML (Linear v1)

recipe: seo_content_strategy
version: 1.0.0
steps:
  - name: founder_intake
    runner: ai
    prompt: prompts/1_founder_intake.md
    input: inputs/founder_intake.input.json
    output: outputs/founder_intake.output.json
    output_schema: schemas/business_profile.schema.v1.json

  - name: icp_definition
    runner: ai
    prompt: prompts/2_icp_definition.md
    input: outputs/founder_intake.output.json
    output: outputs/icp_definition.output.json
    output_schema: schemas/icp.schema.v1.json

  - name: customer_journey
    runner: ai
    prompt: prompts/3_customer_journey.md
    input: outputs/icp_definition.output.json
    output: outputs/customer_journey.output.json
    output_schema: schemas/customer_journey.schema.v1.json

  - name: keyword_discovery
    runner: ai
    prompt: prompts/4_keyword_discovery.md
    input: outputs/customer_journey.output.json
    output: outputs/keyword_discovery.output.json
    output_schema: schemas/raw_keywords.schema.v1.json

  - name: keyword_metrics
    runner: dataforseo
    input: outputs/keyword_discovery.output.json
    output: outputs/keyword_metrics.output.json
    output_schema: schemas/keywords_with_metrics.schema.v1.json

  - name: keyword_clustering
    runner: ai
    prompt: prompts/6_keyword_clustering.md
    input: outputs/keyword_metrics.output.json
    output: outputs/keyword_clustering.output.json
    output_schema: schemas/keyword_clusters.schema.v1.json

  - name: content_strategy
    runner: ai
    prompt: prompts/7_content_strategy.md
    input: outputs/keyword_clustering.output.json
    output: outputs/content_strategy.output.json
    output_schema: schemas/content_strategy.schema.v1.json


⸻

5. MVP Success Criteria
	•	Able to run end-to-end recipe manually in ≤1 hour.
	•	Outputs are valid JSON according to schemas.
	•	Final strategy artifact is specific, actionable, aligned with founder’s vision.
	•	Schema contracts remain stable across 2–3 test runs.

