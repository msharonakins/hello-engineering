
from student_manager import register_student, load_students, save_students, search_students, display_students

students = load_students()

while True:
    print("1. Register student")
    print("2. Display students")
    print("3. Search")
    print("4. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        new_student = register_student()
        students.append(new_student)
        save_students(students)
        print("Student registered successfully.")
    elif choice == "2":
        display_students(students)
    elif choice == "3":
        search_name = input("Enter the name of the student to search for: ")
        found_students = search_students(students, search_name)
        if found_students:
            display_students(found_students)
        else:
            print("No students found.")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")