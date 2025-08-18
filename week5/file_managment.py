file_path = '/Users/el/Dev/cs50p/week5/quotes.txt'

try:
    with open(file_path, 'r') as file:
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print(f"Error: The file {file_path} was not found")
except Exception as e:
    print(f"An error occurred: {e}")