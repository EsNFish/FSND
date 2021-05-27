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
            "type": "String"
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