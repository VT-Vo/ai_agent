from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
def main():
    '''
    pairs = [
        ["calculator", "."],
        ["calculator", "pkg"],
        ["calculator", "/bin"],
        ["calculator", "../"]
    ]
    files_info = list(map(lambda x: get_files_info(*x), pairs))

    for info in files_info:
        print(info)
    '''

    pairs2 = [
        ["calculator", "main.py"],
        ["calculator", "pkg/calculator.py"],
        ["calculator", "/bin/cat"],
        ["calculator", "pkg/does_not_exist.py"]
    ]
    files_content = list(map(lambda x: get_file_content(*x), pairs2))

    for info in files_content:
        print(info)



if __name__ == "__main__":
    main()