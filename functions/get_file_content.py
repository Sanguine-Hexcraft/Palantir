import os
from config import MAX_CHARACTERS

def get_file_content(working_directory, file_path):

    full_path = os.path.join(working_directory, file_path)
    abs_path = os.path.abspath(working_directory)
    full_path = os.path.abspath(full_path)

    if not full_path.startswith(abs_path):
         return f'Error: Cannot read "{full_path}" as it is outside the permitted working directory'

    if not os.path.isfile(full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"' 

    try:
        with open(full_path, "r") as f:
            file_content_string = f.read(MAX_CHARACTERS)

            if os.path.getsize(full_path) > MAX_CHARACTERS:
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARACTERS} characters]' 

            return file_content_string   
            
    except Exception as e:
        return f"Error: {e}"
        
