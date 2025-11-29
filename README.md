# Palantir

Palantir is a tiny command-line AI assistant that pipes your prompt to Google’s Gemini 2.0 Flash model and prints the response directly in your terminal. It is intentionally lightweight so you can peek under the hood, extend it, or plug it into other projects.

## Features
- Single `main.py` entry point with optional `--verbose` token usage output.
- Loads a custom `system_prompt` so you can experiment with guardrails or agent personas.
- Utility helpers in `functions/` for safely listing directories, reading/writing files, and running Python scripts inside a sandboxed folder (`calculator/` is provided for experimentation).
- Simple `tests.py` script that demonstrates how each helper behaves, including common error paths.

## Prerequisites
- Python 3.12+
- A Google AI Studio API key with access to `gemini-2.0-flash-001`
- GNU/Linux or WSL-compatible shell (the repo was built/tested on WSL2)

## Setup
```bash
# from anywhere
git clone <repo-url>
cd Palantir

# optional – keep dependencies isolated
python -m venv .venv
source .venv/bin/activate

# install pyproject dependencies
pip install -e .

# set your Gemini key (or add it to a .env file)
export GEMINI_API_KEY="sk-your-key"
```

If you prefer env files, create `.env` in the project root and add `GEMINI_API_KEY=...`. `python-dotenv` loads it automatically when `main.py` starts.

## Usage
```bash
python main.py "Explain how Palantir works in one sentence"

# optional verbose mode shows prompt/response token counts
python main.py --verbose "Summarize the calculator project"
```
Sample output:
```
================================
Palantir Response:

I'M JUST A ROBOT
```
(The default `system_prompt` currently forces Gemini to respond that way—feel free to edit `prompts.py` with any persona you like.)

## Project Structure
- `main.py` – CLI entry point that builds the prompt list and calls `generate_content`.
- `prompts.py` – Holds the global `system_prompt`.
- `functions/` – Helper modules (`get_files_info`, `get_file_content`, `write_file_content`, `run_python_file`) used by Boot.dev automations and the `tests.py` playground.
- `calculator/` – A sample project used by the helper functions; safe place to run code or read/write files.
- `tests.py` – Manual script with commented scenarios demonstrating the helper APIs.

## Testing & Demos
`tests.py` is intentionally verbose. Uncomment the sections you care about, then run:
```bash
python tests.py
```
The script prints the return values of each helper so you can see both happy paths and validation errors (e.g., trying to execute code outside the sandbox).

## Customizing / Extending
- Swap models by changing `model="gemini-2.0-flash-001"` inside `generate_content`.
- Layer additional conversation turns by appending to the `messages` list before calling `generate_content`.
- Replace the sample `calculator/` directory with your own sandbox to let Palantir manipulate other files safely.

## Troubleshooting
- `Error: GEMINI_API_KEY not set` – ensure the environment variable exists or the `.env` file is loaded.
- `Error: Cannot list ... outside the permitted directory` – the helper functions intentionally refuse to escape the working directory; double-check your paths.
- Hanging or no output – run with `--verbose` to confirm your prompt is being sent and to inspect token counts.

Happy hacking! Let me know what you build with it. 
