import os
from re import S
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from prompts import system_prompt


def main():
    load_dotenv()

    verbose = "--verbose" in sys.argv
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)
    
    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here"')
        print('Example: python main.py "One sentence to explain black metal"')
        print('(rage quitting)')
        sys.exit(1)
    
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)

    ask_palantir = " ".join(args)

    if verbose:
        print(f"User prompt: {ask_palantir}\n")
         
    # Create a new list of AI queries
    messages = [
        types.Content(role="user", parts=[types.Part(text=ask_palantir)]),
    ]

    generate_content(client, messages, verbose)
  
# Get a response from Gemini API with our queries list (messages)
def generate_content(client, messages, verbose):


    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config=types.GenerateContentConfig(system_instruction=system_prompt),
    )
    
    prompt_tokens = response.usage_metadata.prompt_token_count
    response_tokens = response.usage_metadata.candidates_token_count

    # --------- PRINT RESPONSE GOES HERE -----------
    #
    if verbose:
        
        print("================================")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")
        print("================================")
    
    print("================================")
    print(f"Palantir Response:\n\n{response.text}")

if __name__ == "__main__":
    main()
