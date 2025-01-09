def read_file_with_error_handling():
    filename = input("Please enter the filename: ")

    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)

    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")

    except PermissionError:
        print(f"Error: You don't have permission to read the file {filename}.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")


# Example usage
read_file_with_error_handling()
