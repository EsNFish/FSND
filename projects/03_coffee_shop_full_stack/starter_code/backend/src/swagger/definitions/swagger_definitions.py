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

Error400 = {
    "type": "object",
    "properties": {
        "error": {
            "type": "integer",
            "example": 400
        },
        "message": {
            "type": "string",
            "example": "Missing request body"
        },
        "success": {
            "type": "boolean",
            "example": False
        }
    }
}

Error404 = {
    "type": "object",
    "properties": {
        "error": {
            "type": "integer",
            "example": 404
        },
        "message": {
            "type": "string",
            "example": "Drink does not exist"
        },
        "success": {
            "type": "boolean",
            "example": False
        }
    }
}