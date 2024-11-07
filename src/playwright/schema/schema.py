import json
from jsonschema import validate

schema2 = {
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
              "PRESS_LINK": {
                "type": "object",
                "properties": {
                  "name": { "type": "string" }
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
          
          }
        ]
      }
    }
  }
}


schema = {
  "type": "object",
  "properties": {
    "project" : { "type": "string"},
    "url" : { "type": "string"},
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
                      "name": { "type": "string" }
                    },
                    "required": ["name"]
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
                      "name": { "type": "string" },
                      "value": { "type": "string" }
                    },
                    "required": ["name", "value"]
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

def validate_schema(path) -> dict:
    with open(path) as f:
        instance = json.load(f)

    validate(
        instance=instance,
        schema=schema2,
    )

    print("Printing instance...")
    print(instance)

    return instance