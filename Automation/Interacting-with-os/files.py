"""
Working with files using the `OS` library
"""

import os
import datetime

file_size = os.path.getsize("checking_system.py")

print(f"Size: {file_size} bytes")


# Returns time in unix
timestamp = os.path.getmtime("checking_system.py")

FORMATTED_DATETIME = datetime.datetime.fromtimestamp(timestamp)

print(f"Last modified: {FORMATTED_DATETIME}")


# Get Absolute path of the file

abspath = os.path.abspath("checking_system.py")

print(f"File path: {abspath}")
