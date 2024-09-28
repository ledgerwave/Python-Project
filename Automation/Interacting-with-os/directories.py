"""
Working with directories using the `os` library
"""

import os

# equivalent to `pwd` shell command
current_working_directory = os.getcwd()

print(f"CWD : {current_working_directory}")

# creating new directory

# os.mkdir("new_dir")

# os.chdir("new_dir")

# print(os.getcwd())

# moving back to initial directory
# os.chdir("../")

# print(os.getcwd())

# os.rmdir("new_dir")

# list contents of current directory
print(os.listdir("./"))

DIR = "../"

for name in os.listdir(DIR):
    fullname = os.path.join(DIR, name)
    if os.path.isdir(fullname):
        print(f"{fullname.format()} is a directory")
    else:
        print(f"{fullname.format()} is a file")
