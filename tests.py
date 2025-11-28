from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file

print("==================")

# print(get_files_info("calculator", "."))
# print(get_file_content("calculator", "lorem.txt"))

# print(get_file_content("calculator", "main.py"))
# print(get_file_content("calculator", "pkg/calculator.py"))
# print(get_file_content("calculator", "bin/cat"))
# print(get_file_content("calculator", "pkg/does_not_exist.py"))

print(get_files_info("calculator", "pkg"))
print(write_file("calculator", "pkg", ""))