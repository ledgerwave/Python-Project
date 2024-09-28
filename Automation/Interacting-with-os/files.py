"""
Working with files using the `OS` library
"""

import os
import datetime

FILE_NAME = "checking_system.py"

file_size = os.path.getsize(FILE_NAME)

print(f"Size: {file_size} bytes")

# Last modified time, returns time in unix
timestamp = os.path.getmtime(FILE_NAME)

FORMATTED_DATETIME = datetime.datetime.fromtimestamp(timestamp)

print(f"Last modified: {FORMATTED_DATETIME}")

# Get Absolute path of the file
abspath = os.path.abspath(FILE_NAME)

print(f"File path: {abspath}")
