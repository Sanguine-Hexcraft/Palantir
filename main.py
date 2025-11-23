import os
import sys
from dotenv import load_dotenv
from google import genai

def main():
    load_dotenv()
    
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)

    args = sys.argv[1:]

    if len(sys.argv) == 1:
        print("We need to use our words, rage quitting!")
        sys.exit(1)
    else:
        ask_palantir = " ".join(args)

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=ask_palantir
    )

    print("================================")

    
    print(f"Palantir Response:\n\n{response.text}")

    
    print("================================")

    
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")

    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    
    print("================================")


if __name__ == "__main__":
    main()
