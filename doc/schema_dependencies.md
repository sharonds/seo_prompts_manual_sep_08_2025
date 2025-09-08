Perfect 👌 — let’s build the Schema Dependency Map for the Foundation SEO Recipe.
This shows how outputs from Steps 1–6 feed into the final schema of Step 7 (Foundational Content Plan).

⸻

🔗 Schema Dependency Map — Foundation SEO Recipe

Step 1 → Step 2 (Founder Intake → ICP)
	•	business_profile.industry → informs icp.personas[].context
	•	business_profile.services → informs icp.personas[].needs
	•	business_profile.goals → informs icp.personas[].goals

⸻

Step 2 → Step 3 (ICP → Customer Journey)
	•	icp.personas[].pains → influences journey.stages[].questions
	•	icp.personas[].goals → influences journey.stages[].content_needs
	•	icp.personas[].behaviors → influences funnel stage mapping

⸻

Step 3 → Step 4 (Journey → Keyword Discovery)
	•	journey.stages[].content_needs → seed terms for keyword discovery
	•	journey.stages[].questions → expanded into long-tail / FAQ keywords

⸻

Step 4 → Step 5 (Keyword Discovery → Metrics)
	•	raw_keywords.keywords[] → baseline list to enrich with metrics
	•	Optional: raw_keywords.translations[] (if EN→HE pipeline used)

⸻

Step 5 → Step 6 (Metrics → Clustering)
	•	keywords_with_metrics.keywords[].keyword → clustered into topics
	•	keywords_with_metrics.keywords[].volume → influences prioritization
	•	keywords_with_metrics.keywords[].intent → helps map clusters to funnel stage

⸻

Step 6 → Step 7 (Clustering → Foundational Content Plan)
	•	keyword_clusters[].cluster_name → becomes pillars[].clusters[].cluster_name
	•	keyword_clusters[].keywords[] → fills pillars[].clusters[].keywords[]
	•	keyword_clusters[].intent → rolls up into pillars[].funnel_stage + intent_distribution
	•	keyword_clusters[].recommended_content_type → feeds into pillars[].clusters[].recommended_content_type
	•	keyword_clusters[].priority → maps to pillars[].priority
	•	keyword_clusters[].priority_reasoning → maps to pillars[].priority_rationale

⸻

Step 1 + Step 2 (directly to Step 7)
	•	business_profile.goals → used to align pillars[].priority_rationale with business goals
	•	icp.personas[] → used to validate pillar–persona alignment

⸻

✅ Big Picture
	•	Content Plan (Step 7) depends mostly on Step 6 (Clustering), enriched by context from:
	•	Step 5 (metrics → priority)
	•	Step 3 (journey → funnel stage)
	•	Step 1–2 (business goals + ICP → rationale)

⸻

👉 With this map, you can now:
	•	Design each upstream schema knowing exactly which fields must survive to the end.
	•	Spot where data may be thin (Hebrew search volumes, competitor gaps) → and make those fields optional.

⸻

Do you want me to now re-draft the upstream schemas (Steps 1–6) in Foundation mode, so they perfectly align with this final content plan schema?