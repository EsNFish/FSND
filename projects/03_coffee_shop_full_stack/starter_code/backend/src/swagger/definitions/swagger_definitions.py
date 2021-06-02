RecipeItemShort = {
    "type": "object",
    "properties": {
        "color": {
            "type": "string"
        },
        "parts": {
            "type": "integer"
        }
    }
}

RecipeItemLong = {
    "type": "object",
    "properties": {
        "color": {
            "type": "string"
        },
        "parts": {
            "type": "integer"
        },
        "name": {
            "type": "string"
        }
    }
}

DrinkShort = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "recipe": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/RecipeItemShort"
            }
        },
        "title": {
            "type": "string"
        }
    }
}

DrinkLong = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "recipe": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/RecipeItemLong"
            }
        },
        "title": {
            "type": "string"
        }
    }
}

DrinkLongNoId = {
    "type": "object",
    "properties": {
        "recipe": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/RecipeItemLong"
            }
        },
        "title": {
            "type": "string"
        }
    }
}

ResponseShort = {
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "drinks": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/DrinkShort"
            }
        }
    }
}

ResponseLong = {
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "drinks": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/DrinkLong"
            }
        }
    }
}


def error_builder(error, message):
    return {
        "type": "object",
        "properties": {
            "error": {
                "type": "integer",
                "example": error
            },
            "message": {
                "type": "string",
                "example": message
            },
            "success": {
                "type": "boolean",
                "example": False
            }
        }
    }
