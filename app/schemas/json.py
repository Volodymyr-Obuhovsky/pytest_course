# Example of validation by jsonschema

USER_SCHEMA = {
    "type": "object",
    "properties": {
        "user_name": {"type": "string"},
        "email": {"type": "string"},
        "phone": {"type": "string"}
    },
    "required": ["user_name"]
}