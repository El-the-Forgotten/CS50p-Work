import string
from collections import Counter
from pathlib import Path

def unique_and_common_words():
    file1 = input("Enter first filename: ").strip()
    file2 = input("Enter second filename: ").strip()

    def load_words(filename):
        try:
            text = Path(filename).read_text(encoding="utf-8")
        except FileNotFoundError:
            print(f"File not found: {filename}")
            return []
        translator = str.maketrans("", "", string.punctuation)
        cleaned = text.translate(translator).lower()
        return cleaned.split()

    # Load
    words1 = load_words(file1)
    words2 = load_words(file2)

    # Sets and counts
    set1 = set(words1)
    set2 = set(words2)
    counts1 = Counter(words1)
    counts2 = Counter(words2)

    # Derived data
    common = set1 & set2
    unique_all = set1 | set2
    combined_counts = counts1 + counts2

    # Outputs
    print(f"Unique words in {file1}: {len(set1)}")
    print(f"Unique words in {file2}: {len(set2)}")
    print(f"Unique words from both files (union): {len(unique_all)}")
    print(f"Words in common (intersection): {len(common)}")

    # Top 10 common words by each perspective
    common_counts1 = [(w, counts1[w]) for w in common]
    common_counts1.sort(key=lambda x: x[1], reverse=True)

    common_counts2 = [(w, counts2[w]) for w in common]
    common_counts2.sort(key=lambda x: x[1], reverse=True)

    combined_common = [(w, combined_counts[w]) for w in common]
    combined_common.sort(key=lambda x: x[1], reverse=True)

    print("\nTop 10 common words (by frequency in first file):")
    for i, (word, count) in enumerate(common_counts1[:10], start=1):
        print(f"{i:2}. {word}: {count}")

    print("\nTop 10 common words (by frequency in second file):")
    for i, (word, count) in enumerate(common_counts2[:10], start=1):
        print(f"{i:2}. {word}: {count}")

    print("\nTop 10 common words (by combined frequency):")
    for i, (word, count) in enumerate(combined_common[:10], start=1):
        print(f"{i:2}. {word}: {count}")

    print("\nUnique words from both files (alphabetical):")
    for i, word in enumerate(sorted(unique_all), start=1):
        print(f"{i:2}. {word}")

unique_and_common_words()
