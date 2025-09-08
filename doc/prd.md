# PRD — Manual Run (7 Prompts, MVP v1)

## 1. Project Goal

Enable a **manual execution flow** for the SEO Content Strategy recipe using **seven standalone prompts**.

* Objective: validate the **business logic quality** of outputs before investing in automation.
* Execution is **manual**: prompts run one by one in VS Code Copilot Agent.

## 2. Scope (MVP v1 — Manual Mode)

* **7 Prompts** (text files, one per step).
* Each prompt defines: role, task, input, output schema.
* User runs prompts sequentially.
* Input = JSON files (saved per client).
* Output = JSON files (saved per client/date).
* No orchestrator, no evaluators, no ledger, no DB.
* Inputs flow step-to-step based on the dependency map; the initial input is provided by the operator as `business_profile` JSON.
* Standard naming convention for files under `/client/date/` for consistency, e.g., `step01_founder_intake.output.json`.

## 3. Steps (SEO Recipe v1 — Manual Prompts)

1. **Founder Intake → Business Profile**
2. **ICP Definition**
3. **Customer Journey Mapping**
4. **Keyword Discovery**
5. **Keyword Metrics**
6. **Keyword Clustering**
7. **Content Strategy (pillars + calendar)**

## 4. Roles

* **Prompts**: define what the AI should do (role, task, schema).
* **Schemas**: provide strict input/output structure for each step.
* **User (manual operator)**:

  * Runs prompts in order.
  * Supplies input JSON.
  * Saves output JSON into `/client/date/`.

## 5. Deliverables (MVP v1 Manual Run)

* 7 output JSON files per client run.
* Final artifact = **Content Strategy JSON** (pillars, funnel stages, priorities).
* Manual human review of outputs for quality.
* Each output JSON must include a `_meta` field containing `schema_version`, `produced_by`, and `timestamp`.

## 6. Out of Scope

* Orchestrator & automated runners.
* Evaluators + quality scoring.
* Ledger logging.
* Database persistence.
* Client-facing UI.

## 7. Success Criteria

* User can complete **end-to-end recipe manually** in ≤1 hour.
* Outputs are **valid JSON** matching schemas.
* Final strategy output is **specific, actionable, and aligned** with the founder’s vision.
* Reviewer validates cross-step coherence (e.g., ICP personas align with customer journey, clusters align with strategy).
* Unknown values are explicitly labeled as `unknown` where data is sparse.

---

👉 Save this as `/docs/PRD_MANUAL_RUN.md`.

Would you like me to also prepare a **separate PRD for the orchestrator-runner version (v2)** so you have both side by side for when you move beyond manual mode?
