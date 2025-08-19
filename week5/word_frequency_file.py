import string

def word_frequency():
    file_path = input("Enter the filename: ").strip()

    try:
        with open(file_path, 'r') as file:
            text = file.read()
        
        translator = str.maketrans("","", string.punctuation)
        cleaned_text = text.translate(translator).lower()

        words = cleaned_text.split()

        counts={}

        for word in words:
            counts[word] = counts.get(word, 0) + 1

        sorted_items = sorted(counts.items(), key=lambda item: item[1], reverse = True)

        for i, (word, count) in enumerate(sorted_items[:10], start=1):
            print(f"{i}. {word}: {count}")

    except FileNotFoundError:
        print(f"Error: the file {file_path} was not found")
    except Exception as e:
        print(f"An error occurred: {e}")

word_frequency()
