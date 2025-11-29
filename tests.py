from functions import run_python_file
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file_content import write_file_content
from functions.run_python_file import run_python_file

print("==================")

# Get files info tests -----------------------------------------------------------
# print(get_files_info("calculator", "."))
# print(get_file_content("calculator", "lorem.txt"))

# Get file content tests --------------------------------------------------------
# print(get_file_content("calculator", "main.py"))
# print(get_file_content("calculator", "pkg/calculator.py"))
# print(get_file_content("calculator", "bin/cat"))
# print(get_file_content("calculator", "pkg/does_not_exist.py"))

# Get files info tests -----------------------------------------------------------
# print(get_files_info("calculator", "../"))
# print(write_file("calculator", "../", ""))

# Write file content tests -------------------------------------------------------
# print(write_file_content("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))
# print(write_file_content("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))
# print(write_file_content("calculator", "pkg/", "lorem ipsum dolor sit amet"))
# print(write_file_content("calculator", "/tmp/temp.txt", "this should not be allowed"))

# Run python file tests ----------------------------------------------------------
# print(run_python_file("calculator", "../"))
# print(run_python_file("calculator", "test"))
# print(run_python_file("calculator", "lorem.txt"))
# print(run_python_file("calculator", "my_test.py"))
print(run_python_file("calculator", "main.py"))
print(run_python_file("calculator", "main.py", ["3 + 5"]))
print(run_python_file("calculator", "tests.py"))
print(run_python_file("calculator", "../main.py"))
print(run_python_file("calculator", "nonexistent.py"))
print(run_python_file("calculator", "lorem.txt"))

