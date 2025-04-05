name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

print("Hello, " + name)
print(f"You are {age} years old")
print(f"Your height is {height} meters")

x = 10
y = 20
print("The sum of", x, "and", y, "is", x + y)
print(f"The sum of {x} and {y} is {x + y}")
print("The sum of {} and {} is {}".format(x, y, x + y)) 