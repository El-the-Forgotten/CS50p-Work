def get_float():
    while True:
        try:
            total = float(input("Please enter bill total: $"))
            return total
        except ValueError:
            print("Please enter valid dollar amount(numbers only)")

def tip_amount(amount):
    while True:
        try:
            tip = int(input("Tip amount %: "))
            tip = float(tip/100)
            tip = tip*amount
            return tip
        except ValueError:
            print("Please enter only numbers as a percentage")

total = get_float()
tip = tip_amount(total)
grand_total = total + tip

print(f"The grand total including tip for this bill is ${grand_total:.2f}")