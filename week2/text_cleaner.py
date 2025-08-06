sentence = input("Please enter a sentence or phrase: ").strip().lower().replace("don't", "do not").capitalize()

if not sentence.endswith("."):
    sentence+="."

print(f"Here is a cleaned version: {sentence}")