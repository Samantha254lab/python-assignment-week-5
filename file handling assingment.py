def write_to_file():
    """
    Creates a new text file "my_file.txt" and writes content to it.
    """
    try:
        with open("my_file.txt", "w") as file:
            file.write("This is the first line.\n")
            file.write("Here are some numbers: 10, 20, 30.\n")
            file.write("This is the last line for now.\n")
        print("File creation and writing successful.")
    except PermissionError:
        print("Error: You don't have permission to create the file.")
    except Exception as e:  # Catch any other unexpected errors
        print(f"An error occurred: {e}")


def read_from_file():
    """
    Reads the contents of "my_file.txt" and displays them on the console.
    """
    try:
        with open("my_file.txt", "r") as file:
            content = file.read()
            print("File contents:\n", content)
    except FileNotFoundError:
        print("Error: File 'my_file.txt' not found.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")


def append_to_file():
    """
    Opens "my_file.txt" in append mode and writes additional content.
    """
    try:
        with open("my_file.txt", "a") as file:
            file.write("Appending more lines...\n")
            file.write("These lines will be added to the end.\n")
            file.write("Another line for good measure.\n")
        print("Appending to the file successful.")
    except PermissionError:
        print("Error: You don't have permission to write to the file.")
    except Exception as e:
        print(f"An error occurred while appending: {e}")


if __name__ == "__main__":
    # Create the file
    write_to_file()

    # Read the contents (assuming the file was created successfully)
    read_from_file()

    # Append more content
    append_to_file()

    # Read the updated contents
    read_from_file()