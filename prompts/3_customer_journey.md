# Role
Funnel strategist

# Task
Map ICP into a structured buyer journey with Awareness, Consideration, and Decision stages.

# Tool
AI only (no external tools).

# Goal
Link ICP needs to funnel stages for later keyword strategy.

# Input Schema
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

# Output Schema
```json
{
  "type": "object",
  "properties": {
    "stages": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "stage_name": {
            "type": "string"
          },
          "goals": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "questions": {
            "type": "array",
            "items": {
              "type": "string"
            }
          },
          "content_needs": {
            "type": "array",
            "items": {
              "type": "string"
            }
          }
        }
      }
    }
  },
  "required": [
    "stages"
  ]
}
```