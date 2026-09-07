
from student_manager import register_student, load_students, save_students

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