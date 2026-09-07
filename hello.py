print("Hello, Engineering!")
print("Currently learning software engineering, i'm having fun!")
print("This change was made on the branch")
print("Introduction phase 0 is now complete!")
print("Learning professional Git workflow")

name = "Sharon"
age = 16
learning = "Software Engineering"
has_id = True
has_permission = True

print(name)
print(age)
print(learning)

print(type(name))
print(type(age))
print(type(learning))

if age >= 18:
    print("You are an adult.")
elif age >=13:
    print("You are a teenager.")
else:
    print("You are a minor.")

if age >= 18 and has_id:
    print("You can enter.")

if age < 18 or age > 65:
    print("You qualify for the special category.")

if not has_id:
    print("You don't have ID.")

if age >= 18 and has_id:
    print("You may enter the club.")

if age >= 18 or has_permission:
    print("You may enter the event.")

price = 100
discount = 20
final_price = price - discount
print(final_price)
print(type(final_price))

greeting = f"Hello, {name}! You are {age}. Welcome to the world of {learning}."
print(greeting)

user_age =  input("Enter your age: ")
user_age = int(user_age)

print(user_age)
print(type(user_age))

price =  input("Enter the price: ")
price = float(price)

print(price)
print(type(price))

new_name = input("Enter your name: ")
new_age = input("Enter your age: ")
new_age = int(new_age)
programming_language = input("Enter your favorite programming language: ")
introduction = f"Hello, {new_name}! You are {new_age} years old and your favourite programming language is, {programming_language}."
print(introduction)

if new_age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

password = input("Enter a password: ")

while password != "python123":
    password = input("Incorrect Password. Please try again.: ")
    
print("Access granted!")

technologies = ["Python", "Flutter", "Git", "Github"]

for tech in technologies:
    print(f"I am learning {tech}.")

technology = input("Enter a technology: ")
if technology in technologies:
    print("You're already learning this!")
else:
    print("That's not currently on your list.")

tech = input("Enter a technology to add to your list: ")
if tech not in technologies:
    technologies.append(tech)
    print(technologies)
else:
    print("You're already learning this!")

total = 0
numbers = [5,10,15,20,25]

for number in numbers:
    if number > 10:
        total = total + number

print(total)

scores = [45,72,88,51,93,67]
total = 0
count = 0
for score in scores:
    if score >= 60:
        count += 1
        total += score
print(total)
print(count)
print(f"The average score is: {total / count}")

prices = [120,50,300,80,250,40]
total = 0
for price in prices:
    if price > 100:
        total += price
print(f"Total price of items over 100: {total}")

technologies = []

for i in range(3):
    tech = input("Enter a technology you are learning: ")
    technologies.append(tech)

print(f"You are learning the following technologies: {technologies}")

numbers = []
total = 0

for i in range(5):
    num = int(input("Enter a number: "))
    numbers.append(num)
    total += num
    
print(f"The numbers you entered are: {numbers}")
print(f"The total is: {total}")

price = float(input("Enter the price of the item: "))
quantity = int(input("Enter the quantity of the item: "))
discount = float(input("Enter the discount amount: "))
def total_cost(price,quantity):
    return price * quantity

def calculate_discounted_price(price, discount):
    discount_amount = price * discount / 100
    return price - discount_amount
subtotal = total_cost(price, quantity)
final_price = calculate_discounted_price(subtotal, discount)
print(f"The total cost is: {subtotal}")
print(f"The final price after discount is: {final_price}")

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    return total / count

students = {"Alice": 85, "Bob": 52, "Charlie": 73, "David": 41, "Emma": 91}

def analyze_scores(students):
    total = 0
    count = 0
    for score in students.values():
        if score >= 60:
            total += score
            count += 1
    average = total / count
    return average, count

def find_passing_students(students):
    passing_students = []
    for student, score in students.items():
        if score >= 60:
            passing_students.append(student)
    return passing_students

products = {
    "Laptop": 1200,
    "Mouse": 25,
    "Keyboard": 80,
    "Monitor": 350,
    "Headphones": 150
}

def calculate_expensive_products(products):
    total = 0
    for price in products.values():
        if price > 100:
            total += price
    return total

def find_expensive_products(products):
    expensive_products = []
    for product, price in products.items():
        if price > 100:
            expensive_products.append(product)
    return expensive_products

students = {}
for i in range(5):
    name = input("Enter student name: ")
    score = int(input("Enter student score: "))
    students[name] = score

def student_analysis(students):
    passing_students=[]
    total = 0
    count = 0
    for student, score in students.items():
        print(f"{student}: {score}")
        total += score
        if score >= 60:
            passing_students.append(student)   
            count += 1
    average = total /len(students)
    return passing_students, average, count

passing_students, average_score, passing_count = student_analysis(students)
print(f"Names of Passing students: {passing_students}")
print(f"Average score: {average_score}")
print(f"Number of passing students: {passing_count}")

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

def register_students():
    students = []
    number_of_students = int(input("Enter the number of students to register: "))
    for i in range(number_of_students):
        student = register_student()
        students.append(student)
    return students

def calculate_average_score(students):
    if not students:
        return 0
    total_score = 0
    for student in students:
        total_score += student["score"]
    average_score = total_score / len(students)
    return average_score

def get_passing_students(students):
    passing_students = []
    for student in students:
        if student["result"] == "Pass":
            passing_students.append(student["name"])
    return passing_students

registered_students = register_students()
average_score = calculate_average_score(registered_students)
passing_students = get_passing_students(registered_students)
print(f"Average score of registered students: {average_score}")
print(f"Names of passing students: {passing_students}")
