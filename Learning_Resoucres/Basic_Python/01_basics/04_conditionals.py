age = int(input("Enter your age: "))

if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 60:
    print("You are an adult")
else:
    print("You are a senior")

score = int(input("Enter your score: "))
grade = ""

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Your grade is {grade}")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    print(f"{num1} is greater than {num2}")
elif num1 < num2:
    print(f"{num2} is greater than {num1}")
else:
    print("Both numbers are equal") 