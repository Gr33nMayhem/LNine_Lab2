import sys


def replace_assets_in_file(filename):
    try:
        # Read the file content
        with open(filename, 'r') as file:
            content = file.read()

        # Replacement logic
        index = content.find('"assets/')
        while index != -1:
            # Replace "assets/ with {% static 'assets/
            content = content[:index] + "{% static 'assets/" + content[index + 8:]

            # Find the next occurrence of "
            end_quote_index = content.find('"', index + 18)  # Skip ahead by length of inserted text

            # Replace " with '%}
            if end_quote_index != -1:
                content = content[:end_quote_index] + "'%}" + content[end_quote_index + 1:]

            # Move to the next occurrence of "assets/
            index = content.find('"assets/', end_quote_index + 3)

        # Write the modified content back to the file
        with open(filename, 'w') as file:
            file.write(content)

        print(f"File '{filename}' has been updated successfully.")

    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


# Check if the filename was provided as an argument
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python replace_assets.py <filename>")
    else:
        replace_assets_in_file(sys.argv[1])
