import os
import json

from groq import Groq
from tools.expense_tool import add_expense
from tools.tool_definitions import tools

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))


# Connect tool name to Python function
available_functions = {
    "add_expense": add_expense
}


def run_agent(user_input):

    messages = [
        {
            "role": "system",
            "content": """
            You are an expense assistant.

            Extract the following information from the user's expense:
            - amount
            - category
            - description

            Categories can include:
            Food, Travel, Shopping, Bills, Entertainment, Other.

            When all three pieces of information are available,
            call the add_expense tool.
            """
        },
        {
            "role": "user",
            "content": user_input
        }
    ]

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    assistant_message = response.choices[0].message

    # Did Groq call our tool?
    if assistant_message.tool_calls:

        for tool_call in assistant_message.tool_calls:

            function_name = tool_call.function.name

            arguments = json.loads(
                tool_call.function.arguments
            )

            function = available_functions[function_name]

            result = function(**arguments)

            return result

    return assistant_message.content