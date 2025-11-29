import os
from google.genai import types

# AI SCHEMA 
# ---------------
schema_write_file_content = types.FunctionDeclaration(
    name="write_file_content",
    description="Write content to a file within the working directory. Creates the file if it doesn't exist.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file to write, relative to the working directory.",
            ),
            "content": types.Schema(
              type=types.Type.STRING,
              description="Content to write to the file"
            ),
        },
        required=["file_path", "content"],
    ),
)
# ---------------

def write_file_content(working_directory, file_path, content):

  abs_working_dir = os.path.abspath(working_directory)
  abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

  # 1. Security check: Ensure the file is within the working directory
  if not abs_file_path.startswith(abs_working_dir):
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

  # 2. Ensure parent directories exist
  parent_dir = os.path.dirname(abs_file_path)
  if parent_dir and not os.path.exists(parent_dir):
    try:
      os.makedirs(parent_dir, exist_ok=True)
    except Exception as e:
      return f"Error: creating directory: {e}"

  # 3. Don't try to write "to" a directory
  if os.path.exists(abs_file_path) and os.path.isdir(abs_file_path):
    return f'Error: "{file_path}" is a directory, not a file'
  
  # 4. Normal write behavior (create or overwrite)
  try:
    with open(abs_file_path, "w") as f:
      f.write(content)
    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)' 
  except Exception as e:
    return f"Error: writing to file: {e}"

