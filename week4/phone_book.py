def phone_book():
    contacts = {}

    while True:
        name = input("Please enter person's name (or 'done' to stop): ").title()

        if name.lower() == "done":
            # print nicely at the end and return
            for person, number in contacts.items():
                print(f"{person}: {number}")
            return

        # Get a non-empty phone number (loop until valid)
        number = ""
        while not number:
            number = input("Please enter phone number: ").strip()
            if not number:
                print("Please enter a phone number.")

        # Add or update
        if name in contacts:
            print(f"Updating {name}'s number.")
        contacts[name] = number


phone_book()
