import argparse
import os
import json
from call_function import available_functions, call_function
from openai import OpenAI
from dotenv import load_dotenv
from prompts import system_prompt

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="door-code")
parser.add_argument("user_prompt", type=str)
parser.add_argument("--verbose", action="store_true")
args = parser.parse_args()

messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]

for _ in range(20):
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )

    message = response.choices[0].message
    messages.append(message)

    if message.tool_calls:
        for tool_call in message.tool_calls:
            result_message = call_function(tool_call, verbose=args.verbose)
            if not result_message["content"]:
                raise Exception("Empty tool result")
            messages.append(result_message)
            if args.verbose:
                print(f"-> {result_message['content']}")
    else:
        print("Final response:")
        print(message.content)
        break
else:
    print("Error: model did not finish after 20 iterations")
    exit(1)

if args.verbose:
    print("User prompt:", args.user_prompt)
    print("Prompt tokens:", response.usage.prompt_tokens)
    print("Response tokens:", response.usage.completion_tokens)
