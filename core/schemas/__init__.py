from enum import Enum

class Schema(Enum):

    CRETATE_NEW_USER_SCHEMA = {
        "type": "object",
        "required": [
            "code",
            "meta",
            "data",
        ],
        "properties": {
            "code": {"type": "number"},
            "meta": { "type": "null"},
            "data": {
                "type": "object",
                "properties": {
                    "id": {"type": "number"},
                    "name": {"type": "string"},
                    "email": {"type": "string"},
                    "gender": {"type": "string"},
                    "status": {"type": "string"},
                    "created_at": {"type": "string"},
                    "updated_at": {"type": "string"}
                },
                "required": ["id", "name", "email", "gender", "status", "created_at", "updated_at"]
            }
        }
    }