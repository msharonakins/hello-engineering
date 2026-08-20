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



