def shopping_list_creator():
    
    shopping_list = []
    
    while True:
    
        item = input("Please enter an item to add to shopping list or done to stop: ").strip()

        if item.lower() == "done":
            print("Thank you!")
            return shopping_list
        elif item.lower() in (i.lower() for i in shopping_list):
            print(f"{item.title()} has already been added.")
        else:
            shopping_list.append(item.title())
                
shopping_list = shopping_list_creator()

print("Your shopping list: \n", *shopping_list)                