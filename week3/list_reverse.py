words = input("Please enter a sentence or phrase: ")

word_list = words.split()

word_list.reverse()

print(*word_list)