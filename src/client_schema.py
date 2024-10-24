from jsonschema import validate

schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "actions" : {
            # List of actions
            "type": "array",
            "items": {
                # Action object
                "type": "object",
                "properties": {
                    "type": ["BUTTONPRESS", "NAVIGATE"],
                    # "name" refers to innerhtml
                    "name": {"type": "string"},
                    "role": {"type": "string"},
                    "url": {"type": "string"},
                },
                # "required": ["name", "args"],
            },
        },
    },
    "required": ["name"],
}

validate(
    instance={
        "name": "John",
        "age": 30,
        "scores": [70, 90],
        "address": {"street": "Wall Street 1", "postcode": "NY 10005"},
    },
    schema=schema,
)