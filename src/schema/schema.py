import json
from jsonschema import validate


schema = {
  "type": "object",
  "properties": {
    "project" : { "type": "string"},
    "tasks": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "action": {
            "type": "string",
            "enum": ["SIGN_UP", "FOLLOW_USER", "SIGN_IN", "GO_TO_PUBLIC", "GO_TO_USERS", "GO_TO_MY", "POST", "SIGN_OUT", "UNFOLLOW_USER"]
          },
          "subTasks": {
            "type": "array",
            "items": {
              "oneOf": [
                { # PRESS_LINK
                "type": "object",
                "properties": {
                  "PRESS_LINK": {
                    "type": "object",
                    "properties": {
                      "link_text": { "type": "string" }
                    },
                    "required": ["link_text"]
                  }
                },
                "required": ["PRESS_LINK"]
              },
              { # FILL_INPUT
                "type": "object",
                "properties": {
                  "FILL_INPUT": {
                    "type": "object",
                    "properties": {
                      "input_name": { "type": "string" },
                      "value": { "type": "string" }
                    },
                    "required": ["input_name", "value"]
                  }
                },
                "required": ["FILL_INPUT"]
              },
                { # Submit
                    "type": "object",
                    "properties": {
                    "SUBMIT": {
                        "type": "object",
                        "properties": {},
                        "required": [],
                    
                    }
                    },
                    "required": ["SUBMIT"],
                
                }

                ,
                { # Submit input
                    "type": "object",
                    "properties": {
                    "SUBMIT_INPUT": {
                        "type": "object",
                        "properties": {},
                        "required": [],
                    
                    }
                    },
                    "required": ["SUBMIT_INPUT"],
                
                }

                ,
                { # Press button
                    "type": "object",
                    "properties": {
                    "PRESS_BUTTON": {
                        "type": "object",
                        "properties": {
                        "button_name": { "type": "string" }
                        },
                        "required": ["button_name"],
                    
                    }
                    },
                    "required": ["PRESS_BUTTON"],
                
                }

                ,
                { # Navigate to
                    "type": "object",
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
                            
              ] 
            },
          }
        },
        "required": ["action"],
      }
    }
  },
  "required": ["tasks", "project"],
}

with open('test_schema.json') as f:
    instance = json.load(f)

validate(
    instance=instance,
    schema=schema,
)