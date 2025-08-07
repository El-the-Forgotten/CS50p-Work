def number_validator():

    while True: 
        numbers = input("Please enter a list of numbers seperated by commas: ").strip()
        try:
            converted = [float(num.strip()) for num in numbers.split(",")]
            return converted
        except ValueError:
            print("Please enter only valid numbers.")

converted = number_validator()

print("Numbers: ", *converted)
print(f"Sum: {sum(converted)}\nMinimum: {min(converted)}\nMaximum: {max(converted)}\nAvereage: {sum(converted)/len(converted):.2f}")
