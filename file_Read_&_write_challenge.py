def modify_file_content(input_filename, output_filename):
    try:
        # Open the input file for reading
        with open(input_filename, 'r') as infile:
            content = infile.read()

        # Modify the content (For example, convert all text to uppercase)
        modified_content = content.upper()

        # Open the output file for writing
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)

        print(f"Modified content has been written to {output_filename}")

    except FileNotFoundError:
        print(f"Error: The file {input_filename} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
input_filename = 'input.txt'  # Replace with your input file name
output_filename = 'output.txt'  # Replace with your desired output file name
modify_file_content(input_filename, output_filename)
