def grading_dictionary():
    
    grades = {}

    while True:
        name = input("Please enter student name: ").strip().title()
        if name.lower() == "done":
            if not grades:
                print("No grades were given")
                return
            print("\nStudent Grades: ")
            for person, grade in grades.items():
                avg = sum(grade) / len(grade)
                maximum = max(grade)
                minimum = min(grade)
                print(f"{person} - Average: {avg:.2f}, Highest: {maximum:.2f}, Lowest: {minimum:.2f}")
            return
        while True:
            score = input(f"Please enter a grade for {name.title()}(or 'done' to stop): ").strip()
            if not score:
                print("Please enter score or 'done'.")
                continue
            if score.lower() == "done":
                break
            try:
                graded = float(score)
                grades.setdefault(name, []).append(graded)
            except ValueError:
                print("Please enter a valid grade(number).")

grading_dictionary()