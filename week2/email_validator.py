def email_validator(email):

    first_check = "@"
    second_check = "."
    at_count = 0
    period_count = 0
    valid = "Valid"
    invalid = "Invalid"

    for char in email:
        if char in first_check:
            at_count+=1
        if char in second_check:
            period_count+=1
    if email.rfind("@") < email.rfind(".") and at_count == 1 and period_count >= 1:
        print("Valid email")
        return valid
    else:
        print("Invalid email")
        return invalid

email_address = input("Please enter a valid email address: ")

print(f"{email_address} is {email_validator(email_address)}")