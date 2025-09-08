# Role
Marketing strategist

# Task
Define 2–4 Ideal Customer Profiles (ICPs) with demographics, pain points, motives, and channel habits.

# Tool
AI only (no external tools).

# Goal
Identify realistic ICPs based on the business profile.

# Input Schema
```json
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string"
    },
    "industry": {
      "type": "string"
    },
    "business_model": {
      "type": "string",
      "enum": [
        "B2B",
        "B2C",
        "B2B2C",
        "Marketplace"
      ]
    },
    "core_products": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "value_props": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "goals": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "company_name",
    "industry",
    "business_model",
    "core_products"
  ]
}
```

# Output Schema
```json
{
  "type": "object",
  "properties": {
    "segments": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "demographics": {
      "type": "object",
      "properties": {
        "age_range": {
          "type": "string"
        },
        "location": {
          "type": "string"
        },
        "job_titles": {
          "type": "array",
          "items": {
            "type": "string"
          }
        }
      }
    },
    "pain_points": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "buying_motives": {
      "type": "array",
      "items": {
        "type": "string"
      }
    }
  },
  "required": [
    "segments",
    "pain_points"
  ]
}
```