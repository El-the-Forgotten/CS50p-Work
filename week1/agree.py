agreed = False

while agreed == False:
    answer = input("Do you agree?").strip().lower()
    if answer == "yes":
        agreed = True
        print("Agreed")
    elif answer == "y":
        agreed = True
        print("Agreed")
    elif answer == "no":
        agreed == False
        print("Not agreed")
    elif answer == "n":
        agreed = False
        print("Not agreed")
    else:
        agreed = False
        print("Please enter Y/Yes or N/No")
