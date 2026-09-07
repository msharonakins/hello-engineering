import json

def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file)

def get_score():
    while True:
        try:
            score = int(input("Enter score: "))
            if validate_score(score):
                return score
            print("Please enter a valid number between 0 and 100.")
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

def validate_score(score):
    if score < 0 or score > 100:
        return False
    return True

def register_student():
    name = input("Enter name: ")
    age = int(input("Enter age: "))

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
