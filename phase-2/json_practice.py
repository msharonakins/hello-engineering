import json

from hello import register_student

def load_students():
    try:
        with open("students.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []
    
def save_students(students):
    with open("students.json", "w") as file:
        json.dump(students, file)

students = load_students()

while True:
    print("1. Register student")
    print("2. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        new_student = register_student()
        students.append(new_student)
        save_students(students)
        print(students)
    elif choice == "2":
        break
    else:
        print("Invalid choice.")