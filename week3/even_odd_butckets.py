def integer_list(numbers):

    evens = []
    odds = []

    cleaned_num = numbers.split(",")

    for nums in cleaned_num:
        nums = nums.strip()
        try:
            nums = int(nums)
            if nums % 2 == 0:
                evens.append(nums)
            else:
                odds.append(nums)
        except ValueError:
            print(f"{nums} is not an integer.")
    return evens, odds

numbers = input("Please enter a list of integers with commas seperating each: ").strip()

evens, odds = integer_list(numbers)

print(f"Evens:", *evens)
print(f"Odds:", *odds)