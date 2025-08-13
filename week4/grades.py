def grade_book():

    grades = {}

    while True:
        name = input("Please enter a name (or 'done' to stop): ").strip().title()
        if name.lower() == "done":
            if not grades:
                print("No grades entered.")
                return
            print ("\nStudent Grades:")
            for person, scores in grades.items():
                avg = sum(scores) / len(scores)
                print(f"{person.title()}: {avg:.2f}")
            return
        while True:
            grade = input(f"Please enter a grade for {name.title()}: ")
            try:
                graded = float(grade)
                break
            except ValueError:
                print("Please enter a valid grade(number).")
        grades.setdefault(name, []).append(graded)
        if len(grades[name]) > 1:
            print(f"Another grade added for {name.title()} (now {len(grades[name])} total)")
        else:
            print(f"First grade added for {name.title()}.")

grade_book()