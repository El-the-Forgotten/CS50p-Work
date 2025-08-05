def get_number():
    valid = False

    while valid == False:
        answer = input("Please enter and integer: ")
        try:
            int(answer)
            answer = int(answer)
            valid = True
            return answer
        except ValueError:
            print("Please enter a valid integer")
            valid = False
        
number1 = get_number()
number2 = get_number()

print(f"The sum of both number is: {number1 + number2}")

