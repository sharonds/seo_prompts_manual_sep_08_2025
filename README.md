# Manual Pipeline Execution Guide

This folder contains everything needed to run the 7-step SEO strategy pipeline **manually** in VS Code (with Copilot Agent + MCPs).

## 📂 Structure
- /prompts/ → 7 detailed prompts (schemas embedded) + summarizer.md
- /schemas/ → JSON schemas for each step
- /client_example/inputs/ → sample input file
- /client_example/outputs/ → empty output files to fill
- README.md → this guide

## 🚀 How to Run
1. Open VS Code with Copilot Agent.
2. Pick the right prompt file from /prompts/ (e.g., 1_founder_intake_to_profile.md).
3. Provide the input JSON (from /client_example/inputs/) as context.
4. Run the prompt. Copilot will output JSON following the schema.
5. Save the result in /client_example/outputs/ with the correct filename.
6. Repeat for all 7 steps.
7. Optionally run summarizer.md on each JSON to generate plain-text explanations.

## ✅ Flow
1. Founder Intake → Business Profile
2. ICP Definition
3. Customer Journey Mapping
4. Keyword Discovery (AI + DataForSEO/Firecrawl if available)
5. Keyword Metrics (DataForSEO + fallback AI)
6. Keyword Clustering (AI)
7. Content Strategy (AI)

---

This setup is optimized for **speed + quality** (manual mode). Automation can be added later if needed.
