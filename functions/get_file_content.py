import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
        abs_working = os.path.abspath(working_directory)
        if not abs_working.endswith(os.sep):
              abs_working += os.sep
        target_path = os.path.join(working_directory, file_path)
        abs_file = os.path.abspath(target_path)

        if not abs_file.startswith(abs_working):
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        elif not os.path.isfile(target_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        try:
            with open(target_path, "r") as f:
                    file_content = f.read(MAX_CHARS + 1)
                    if len(file_content) > MAX_CHARS:
                        file_content = file_content[:MAX_CHARS] + f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
                    return file_content
        except Exception as e:
             return f'Error: {e}'