tools = [
    {
        "type": "function",
        "function": {
            "name": "add_expense",
            "description": "Add an expense to the Excel file.",
            "parameters": {
                "type": "object",
                "properties": {
                    "amount": {
                        "type": "number",
                        "description": "The amount of money spent."
                    },
                    "category": {
                        "type": "string",
                        "description": "The expense category such as Food, Travel, Shopping, Bills, or Other."
                    },
                    "description": {
                        "type": "string",
                        "description": "A short description of what the money was spent on."
                    }
                },
                "required": [
                    "amount",
                    "category",
                    "description"
                ]
            }
        }
    }
]