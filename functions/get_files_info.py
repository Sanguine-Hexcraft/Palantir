import os 

def get_files_info(working_directory, directory="."):

    full_path = os.path.join(working_directory, directory)

    if not os.path.abspath(full_path).startswith(os.path.abspath(working_directory)):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(full_path):
        return f'Error: "{directory}" is not a directory'

    try:
        lines = []
        
        for i in os.listdir(full_path):
        
            item_path = os.path.join(full_path, i)

            size = os.path.getsize(item_path)

            is_dir =  os.path.isfile(item_path)

            lines.append(f"- {i}: file_size: {size} bytes, is_dir={is_dir}")
    
        if directory == ".":
            intro_line = "Result for current directory:"
        else:
            intro_line = f"Result for {directory} directory:"

        return intro_line + "\n" + "\n".join(lines)

    except Exception as e:
        return f"Error: {e}"