import os

def get_files_info(working_directory, directory="."):
    try:
        target_path = os.path.join(working_directory, directory)
        abs_target = os.path.abspath(target_path)
        abs_working = os.path.abspath(working_directory)

        inside = abs_target == abs_working or abs_target.startswith(abs_working + os.sep)
        if not inside:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(abs_target):
            return f'Error: "{directory}" is not a directory'

        dir_contents = os.listdir(abs_target)
        formatted_contents = list()
        for content in dir_contents:
            path_to_file = os.path.join(abs_target, content)
            file_size = os.path.getsize(path_to_file)
            is_dir = os.path.isdir(path_to_file)
            formatted_contents.append(f"- {content}: file_size={file_size} bytes, is_dir={is_dir}")
    except Exception as e:
        return f"Error: {e}"
    return "\n".join(formatted_contents).strip()
