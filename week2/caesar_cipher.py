def encryption(text, number):
    encrypted = ""

    for char in text:
        if char.isupper():
            encrypted += chr(((ord(char) -65 + number)%26)+65)
        elif char.islower():
            encrypted += chr(((ord(char)-97)%26)+97)
        else:
            encrypted +=char

    return encrypted

sentence = input("Please enter a sentence: ")
number = int(input("How many places would you like to move? "))

result = encryption(sentence, number) 

print(f"Encrypted: {result}")