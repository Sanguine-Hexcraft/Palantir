import os

def write_file(working_directory, file_path, content):

  full_path = os.path.join(working_directory, file_path)
  abs_path = os.path.abspath(working_directory)
  full_path = os.path.abspath(full_path)

  if not full_path.startswith(abs_path):
    return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

  return f"full path:::: {full_path}, working path::: {abs_path}" 