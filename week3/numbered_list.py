items = input("Please enter items with commas seperating them: ")

clean_items = [item.strip() for item in items.split(",")]

for i, item in enumerate(clean_items, start=1):
    print(f"{i}. {item}")