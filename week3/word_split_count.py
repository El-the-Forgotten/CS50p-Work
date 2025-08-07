text = input("Please enter a sentence or phrase: ")

words = text.split()

word_count = 0

for word in words:
    word_count+=1
    print(f"{word}")

print(f"Total words: {word_count}")