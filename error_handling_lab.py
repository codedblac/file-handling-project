from pathlib import Path




def read_file(filename: str, encoding: str = "utf-8") -> str | None:
    """
    Read and return the contents of a file.

    Args:
        filename (str): Path to the file.
        encoding (str): File encoding.

    Returns:
        str | None: File contents if successful, otherwise None.
    """
    try:
        file_path = Path(filename)

        if not file_path.exists():
            raise FileNotFoundError(f"{filename} does not exist.")

        if not file_path.is_file():
            raise IsADirectoryError(f"{filename} is not a file.")

        return file_path.read_text(encoding=encoding)

    except FileNotFoundError as e:
        print(f"Error: {e}")

    except PermissionError:
        print(f"Error: You don't have permission to read '{filename}'.")

    except IsADirectoryError:
        print(f"Error: '{filename}' is a directory, not a file.")

    except UnicodeDecodeError:
        print(f"Error: Unable to decode '{filename}'. Try a different encoding.")

    except Exception as e:
        print(f"Unexpected error: {e}")

    return None





def main():
    filename = input("Please enter the filename: ").strip()

    if not filename:
        print("Error: Filename cannot be empty.")
        return

    content = read_file(filename)

    if content is not None:
        print("\nFile content:\n")
        print(content)


if __name__ == "__main__":
    main()


