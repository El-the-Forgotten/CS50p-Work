def count_vowels(phrase):

    vowels = "aeiou"
    count = 0
    letters = []

    for char in phrase:
        if char in vowels:
            count +=1
            letters.append(char)
            
    return count, letters
    
input_phrase = input("Please enter a word or phrase: ").lower()
vowel_count = count_vowels(input_phrase)

print(f"The number of vowels: {vowel_count}")