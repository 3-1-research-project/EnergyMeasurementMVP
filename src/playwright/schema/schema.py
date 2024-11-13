import json
from jsonschema import validate

schema = {
  "type": "object",
  "properties": {
    "project": {
      "type": "string"
    },
    "url": {
      "type": "string",
      "format": "uri"
    },
    "tasks": {
      "type": "object",
      "properties": {
        "SIGN_UP": { "$ref": "#/definitions/taskArray" },
        "FOLLOW_USER": { "$ref": "#/definitions/taskArray" },
        "SIGN_IN": { "$ref": "#/definitions/taskArray" },
        "GO_TO_PUBLIC": { "$ref": "#/definitions/taskArray" },
        "GO_TO_USERS": { "$ref": "#/definitions/taskArray" },
        "GO_TO_MY": { "$ref": "#/definitions/taskArray" },
        "POST": { "$ref": "#/definitions/taskArray" },
        "SIGN_OUT": { "$ref": "#/definitions/taskArray" },
        "UNFOLLOW_USER": { "$ref": "#/definitions/taskArray" }
      },
    }
  },
  "required": ["project", "url", "tasks"],
  "definitions": {
    "taskArray": {
      "type": "array",
      "items": {
        "type": "object",
        "oneOf": [
            {
                "properties": {
              "NAVIGATE_TO": {
                "type": "object",
                "properties": {
                  "url": { "type": "string" }
                },
                "required": ["url"],
              }
            },
            "required": ["NAVIGATE_TO"],
          },
          {
            "properties": {
              "PRESS_LINK": {
                "type": "object",
                "properties": {
                  "name": { "type": "string" },
                  "value": { "type": "string" }
                },
                "required": ["name"],
              }
            },
            "required": ["PRESS_LINK"],
          },
          {
            "properties": {
              "FILL_INPUT": {
                "type": "object",
                "properties": {
                  "name": { "type": "string" },
                  "value": { "type": "string" }
                  
                },
                "required": ["name", "value"],
              }
            },
            "required": ["FILL_INPUT"],
          
          },
          {
            "properties": {
              "SUBMIT": {
                "type": "object",
                "properties": {},
              
              }
            },
            "required": ["SUBMIT"],
          
          },
          # submit input
          {
            "properties": {
              "SUBMIT_INPUT": {
                "type": "object",
                "properties": {},
              
              }
            },
            "required": ["SUBMIT_INPUT"],  
          },
         
          # press button
          {
            "properties": {
              "PRESS_BUTTON": {
                "type": "object",
                "properties": {
                  "name": { "type": "string" }
                },
                "required": ["name"],
              }
            },
            "required": ["PRESS_BUTTON"],  
          },
          
        ]
      }
    }
  }
}

def validate_schema(path) -> dict:
    with open(path) as f:
        instance = json.load(f)

    validate(
        instance=instance,
        schema=schema,
    )

    return instance