def star_numbers():

    array = []

    while True:
        number =(input("Enter numbers or n or no to stop: "))
        try:
            int(number)
            number = int(number)
            array.append(number)
        except ValueError:
            if number.lower() in ["n", "no"]:
                return array
            print("Please enter an integer or n or no to stop")

def star_print(stars):

    star = "*"

    for i in stars:
        number = i * star
        print(number)

star_print(star_numbers())
