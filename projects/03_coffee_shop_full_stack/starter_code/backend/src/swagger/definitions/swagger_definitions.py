RecipeItem = {
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

Drink = {
    "type": "object",
    "properties": {
        "id": {
            "type": "integer"
        },
        "recipe": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/RecipeItem"
            }
        },
        "title": {
            "type": "string"
        }
    }
}

Response = {
    "type": "object",
    "properties": {
        "success": {
            "type": "boolean"
        },
        "drinks": {
            "type": "array",
            "items": {
                "$ref": "#/definitions/Drink"
            }
        }
    }
}
