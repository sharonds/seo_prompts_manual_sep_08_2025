# Role
Content strategist

# Task
Convert clusters into content pillars with funnel stages, narratives, and priorities.

# Tool
AI only.

# Goal
Produce strategic content pillars that balance funnel coverage and business priorities.

# Input Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "cluster_name": {
        "type": "string"
      },
      "keywords": {
        "type": "array",
        "items": {
          "type": "string"
        }
      },
      "avg_volume": {
        "type": "integer"
      },
      "business_priority_score": {
        "type": "integer",
        "minimum": 1,
        "maximum": 5
      },
      "confidence_level": {
        "type": "number",
        "minimum": 0,
        "maximum": 1
      }
    },
    "required": [
      "cluster_name",
      "keywords"
    ]
  }
}
```

# Output Schema
```json
{
  "type": "object",
  "properties": {
    "pillars": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "pillar": {
            "type": "string"
          },
          "theme_statement": {
            "type": "string"
          },
          "clusters": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "funnel_stage": {
            "type": "string"
          },
          "priority_score": {
            "type": "integer",
            "minimum": 1,
            "maximum": 5
          }
        }
      }
    }
  },
  "required": [
    "pillars"
  ]
}
```