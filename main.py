import sys
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    inputs = sys.argv

    if len(inputs) < 2:
        print("No input entered, use format:\nuv run main.py [input]")
        sys.exit(1)

    messages = [types.Content(role="user", parts=[types.Part(text=inputs[1])])]

    response = client.models.generate_content(
        model = "gemini-2.0-flash-001",
        contents = messages
    )
    print(response.text)
    if (len(inputs) > 2 and inputs[2] == "--verbose"):
        print(f"User prompt: {inputs[1]}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    


if __name__ == "__main__":
    main()
