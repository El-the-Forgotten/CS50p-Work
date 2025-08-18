file_path = '/Users/el/Dev/cs50p/week5/notes.txt'
blank = ""
yes = "y yes"
no = "n no"

try:
    with open(file_path, 'x') as file:
        print(f"File {file_path} created.")
except FileExistsError:
    while True:
        answer = input(f"File {file_path} already exists. Overwrite?(y/n)\n").strip()
        if answer.lower() in yes:
            try:
                with open(file_path, 'w') as file:
                    print("Overwriting file...")
                    file.write(blank)
                    break
            except IOError as e:
                print(f"Error: {e}")
                break
        elif answer.lower() in no:
            break
        else:
            print("Please type Y/YES or N/NO")
    

try:
    with open(file_path, "a") as file: 
        while True:
            print(f"Enter lines to add to file {file_path}. Type 'done' to finish.")
            line = input(f">").strip()

            if line.lower() == "done":
                break

            file.write(line + "\n")
except Exception as e:
    print(f"The error {e} has occurred.")

try:
    with open(file_path, 'r') as file:
        for i, lines in enumerate(file,start=1):
            print(f"{i}: {lines}")
except FileExistsError:
    print(f"The file {file_path} does not exist")
except Exception as e:
    print(f"An error occurred: {e}")