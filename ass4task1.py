# read_file_with_error_handling.py

def read_file():
    try:
        with open("sample.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("Error: The file 'sample.txt' was not found.")

# Run the function
read_file()
