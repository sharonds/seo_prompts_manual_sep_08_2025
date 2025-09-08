# Role
Business strategist

# Task
Transform founder notes into a structured business profile.

# Tool
AI only (no external tools).

# Goal
Normalize vague founder input into a structured business profile usable for downstream steps.

# Input Schema
```json
{
  "type": "object",
  "properties": {
    "company_name": {
      "type": "string"
    },
    "founder_vision": {
      "type": "string"
    },
    "products_services": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "target_market": {
      "type": "string"
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
    "founder_vision",
    "products_services"
  ]
}
```

# Output Schema
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