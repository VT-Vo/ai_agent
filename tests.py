from functions.get_files_info import get_files_info
def main():
    pairs = [
        ["calculator", "."],
        ["calculator", "pkg"],
        ["calculator", "/bin"],
        ["calculator", "../"]
    ]
    files_info = list(map(lambda x: get_files_info(*x), pairs))
    for info in files_info:
        print(info)

if __name__ == "__main__":
    main()