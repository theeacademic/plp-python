import os


def read_file_contents(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"File not found: {file_path}")
    with open(file_path, "r", encoding="utf-8") as file:
        return file.readlines()


def write_modified_contents(original_path, lines):
    base, ext = os.path.splitext(original_path)
    output_path = f"{base}_modified{ext or '.txt'}"
    with open(output_path, "w", encoding="utf-8") as file:
        for idx, line in enumerate(lines, start=1):
            file.write(f"{idx}: {line}")
    return output_path


if __name__ == "__main__":
    try:
        input_path = input("Enter the filename to read: ").strip()
        contents = read_file_contents(input_path)
        output_path = write_modified_contents(input_path, contents)
    except FileNotFoundError as e:
        print(str(e))
    except PermissionError:
        print("Permission denied: Unable to read or write the specified file.")
    except OSError as e:
        print(f"OS error: {e}")
    else:
        print(f"Modified file written to: {output_path}")


