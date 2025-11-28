import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    
    abs_working_directory = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.exists(abs_file_path): 
        return f'Error: File "{file_path}" not found.'

    if not abs_file_path.endswith(".py"):
        return f'"{file_path}" is not a Python file.'    

    # subprocess.run("python", )