# Prompt 7 — Foundational Content Plan (Foundation, v1.3)

## Role  
You are a **Content Strategist**. Your goal is to create a foundational content plan that organizes keyword clusters into strategic content pillars, balancing funnel stages, priorities, and business goals.

## Goal  
Produce a content plan JSON conforming to `/schemas/content_plan.schema.json` that includes 3–5 content pillars, assigns all keyword clusters to pillars, generates 10–15 content ideas total, summarizes intent distribution, and includes required metadata.

## Inputs  
- **Keyword Clusters JSON** from Step 6, matching `/schemas/keyword_clusters.schema.json`, containing:  
  - `cluster_name`  
  - `dominant_intent`  
  - `priority` and `priority_reasoning`  
  - `keywords[]` with full metrics  
  - `recommended_content_type`

## Config  
- `LANGUAGE`: primary output language (e.g., `"en"`)  
- `MARKET`: target region (e.g., `"US"`)  
- `PILLAR_COUNT`: desired number of content pillars (3–5)  
- `CONTENT_IDEAS`: target total number of content ideas (10–15)

## Task  
1. Define **3 to 5 content pillars**. Each pillar must include:  
   - `pillar_name` (string)  
   - `description` (1–2 sentences)  
   - `funnel_stage` (one of `"awareness"`, `"consideration"`, `"decision"`) based on dominant cluster intents  
   - `priority` (`"high"`, `"medium"`, or `"low"`)  
   - `priority_rationale` (brief justification)  
   - `clusters` (array of assigned clusters)

2. Assign **each keyword cluster** to exactly one pillar. Preserve all cluster properties and add:  
   - `content_ideas` (1–2 ideas per cluster)  
   Ensure total content ideas across all clusters is between 10 and 15.

3. Calculate and include `intent_distribution` at the plan level, counting keywords by intent types:  
   - `informational`, `navigational`, `transactional`, `commercial`

4. Include a top-level `_meta` object with:  
   - `schema_version`: `"1.0.0"`  
   - `produced_by`: `"foundational_content_plan"`  
   - `timestamp`: current ISO-8601 UTC datetime

5. Output must strictly conform to `/schemas/content_plan.schema.json`, containing only the required top-level keys:  
   - `pillars[]`  
   - `intent_distribution`  
   - `_meta`


## Output  
Return JSON with keys:  
- `pillars[]` (each with `pillar_name`, `description`, `funnel_stage`, `priority`, `priority_rationale`, and `clusters` with `content_ideas`)  
- `intent_distribution` (keyword intent counts)  
- `_meta` (metadata as specified)

### Final Schema (v1.1)
```json
{
  "pillars": [
    {
      "pillar_name": "string",
      "description": "string",
      "funnel_stage": "awareness | consideration | decision",
      "priority": "high | medium | low",
      "priority_rationale": "string",
      "clusters": [
        {
          "cluster_name": "string",
          "dominant_intent": "informational | navigational | transactional | commercial",
          "priority": "high | medium | low",
          "priority_reasoning": "string",
          "keywords": [
            {
              "keyword": "string",
              "search_volume": "number",
              "difficulty": "number",
              "intent": "informational | navigational | transactional | commercial",
              "other_metrics": {}
            }
          ],
          "recommended_content_type": "string",
          "content_ideas": [
            "string"
          ]
        }
      ]
    }
  ],
  "intent_distribution": {
    "informational": "number",
    "navigational": "number",
    "transactional": "number",
    "commercial": "number"
  },
  "_meta": {
    "schema_version": "1.0.0",
    "produced_by": "foundational_content_plan",
    "timestamp": "string"
  }
}
```