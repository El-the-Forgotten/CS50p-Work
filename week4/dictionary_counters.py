import string

counts = {}

sentence = input("Please enter a sentence or phrase: ").strip().lower()

translator = str.maketrans('','', string.punctuation)

cleaned_sentence = sentence.translate(translator)

words = cleaned_sentence.split()

for word in words:
    counts[word] = counts.get(word, 0)+1

sorted_items = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

for word, count in sorted_items:
    print(f"{word}: {count}")