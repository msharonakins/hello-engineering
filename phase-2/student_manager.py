import json

def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print("Could not read student data. Starting with an empty list.")
        return []
    
def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file)

def get_age():
    while True:
        try:
            age = int(input("Enter age: "))
            if age >= 0:
                return age
            print("Please enter a valid age (0 or older).")
        except ValueError:
            print("Please enter a number.")

def get_score():
    while True:
        try:
            score = int(input("Enter score: "))
            if score < 0 or score > 100:
                print("Please enter a valid number between 0 and 100.")
            else:
                return score
        except ValueError:
            print("Please enter a number.")

def get_result(score):
    if score >= 60:
        return "Pass"
    else:
        return "Fail"

def get_grade(score):
    if score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    return grade

def get_name():
    while True:
        name = input("Enter name: ").strip()
        if name:
            return name
        print("Please enter a name.")

def register_student():
    name = get_name()
    age = get_age()
    score = get_score()
    result = get_result(score)
    grade = get_grade(score)

    student = {
        "name": name,
        "age": age,
        "score": score,
        "result": result,
        "grade": grade
    }

    return student

def search_students(students, search_name):
    search_name = search_name.lower()
    return [student for student in students if student["name"].lower() == search_name]

def display_students(students):
    if not students:
        print("No students registered.")
        return

    print("\n=== Registered Students ===")
    print("--------------------------")
    for student in students:
        print(f"Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Score: {student['score']}")
        print(f"Result: {student['result']}")
        print(f"Grade: {student['grade']}")
        print("--------------------------")
        print()
