# Role
SEO strategist

# Task
Group keywords into semantic clusters and assign business priority.

# Tool
AI only.

# Goal
Organize keywords into meaningful clusters tied to business relevance.

# Input Schema
```json
{
  "type": "array",
  "items": {
    "type": "object",
    "properties": {
      "keyword": {
        "type": "string"
      },
      "search_volume": {
        "type": "integer"
      },
      "cpc": {
        "type": "number"
      },
      "competition": {
        "type": "number"
      },
      "trend": {
        "type": "array",
        "items": {
          "type": "integer"
        }
      },
      "metrics_source": {
        "type": "string",
        "enum": [
          "dataforseo",
          "ai_estimate"
        ]
      },
      "confidence_level": {
        "type": "number",
        "minimum": 0,
        "maximum": 1
      }
    },
    "required": [
      "keyword",
      "search_volume",
      "metrics_source"
    ]
  }
}
```

# Output Schema
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