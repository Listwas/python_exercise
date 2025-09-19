#Check File is Empty or Not
import os

def is_file_empty(path):
    try:
        file_size = os.path.getsize(path)
        if file_size == 0:
            return "file is empty"
        return f"file size: {file_size} bytes"
    except Exception as e:
        return e

usr_input = input("path to file: ")
print(is_file_empty(usr_input))

