# File Creation
def create_file():
    try:
        # Open "my_file.txt" in write mode ('w')
        with open("my_file.txt", "w") as file:
            # Write three lines of text to the file
            file.write("Learning python is fun!\n")
            file.write("You just need to create time like 3 to 4 hours a day.\n")
            file.write("For you to be successful.\n")
        print("File 'my_file.txt' created and initial content written successfully.")
    except Exception as e:
        print(f"Error occurred while creating the file: {e}")

# File Reading and Display
def read_file():
    try:
        # Open "my_file.txt" in read mode ('r')
        with open("my_file.txt", "r") as file:
            # Read and display the contents of the file
            contents = file.read()
            print("Contents of 'my_file.txt':")
            print(contents)
    except FileNotFoundError:
        print("File 'my_file.txt' not found.")
    except PermissionError:
        print("Permission denied to access 'my_file.txt'.")

# File Appending
def append_to_file():
    try:
        # Open "my_file.txt" in append mode ('a')
        with open("my_file.txt", "a") as file:
            # Append three additional lines of text to the file
            file.write("Develop passion for it.\n")
            file.write("Its hard in 1, 2, 3 weeks of starting but finally you get used to it.\n")
            file.write("It has alot of benefit at the end, give it a try.\n")
        print("Additional content appended to 'my_file.txt'.")
    except Exception as e:
        print(f"Error occurred while appending to the file: {e}")

# Error Handling (Main Execution)
if __name__ == "__main__":
    create_file()  # Create the file and write initial content
    read_file()    # Read and display the file contents
    append_to_file()  # Append additional content to the file

