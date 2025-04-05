def greet(name):
    print(f"Hello, {name}!")

greet("John")

def add(a, b):
    return a + b

result = add(5, 3)
print(result)

def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

grade = calculate_grade(85)
print(grade)

def average(*numbers):
    return sum(numbers) / len(numbers)

avg = average(1, 2, 3, 4, 5)
print(avg)

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i)) 