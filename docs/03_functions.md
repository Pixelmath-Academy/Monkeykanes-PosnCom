# Python Functions

This section covers functions and modular programming in Python.

## Contents

1. [Basic Functions](#basic-functions)
2. [Function Parameters](#function-parameters)
3. [Return Values](#return-values)
4. [Recursion](#recursion)

## Basic Functions

File: `03_functions/01_functions.py`

Functions are reusable blocks of code that perform specific tasks.

### Key Concepts:
- Function definition using `def`
- Function calling
- Function scope
- Local and global variables

### Examples:
```python
# Basic function definition and calling
def greet(name):
    print(f"Hello, {name}!")

greet("John")

# Function with return value
def add(a, b):
    return a + b

result = add(5, 3)
print(result)
```

## Function Parameters

### Types of Parameters:
- Required parameters
- Default parameters
- Variable-length arguments (*args)
- Keyword arguments (**kwargs)

### Examples:
```python
# Function with default parameter
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("John")
greet("John", "Hi")

# Function with variable arguments
def average(*numbers):
    return sum(numbers) / len(numbers)

avg = average(1, 2, 3, 4, 5)
print(avg)
```

## Return Values

Functions can return:
- Single values
- Multiple values (as tuples)
- None (implicitly)

### Examples:
```python
# Function returning multiple values
def get_coordinates():
    x = 10
    y = 20
    return x, y

x, y = get_coordinates()
print(f"X: {x}, Y: {y}")

# Function with conditional return
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
```

## Recursion

Recursion is when a function calls itself.

### Key Concepts:
- Base case
- Recursive case
- Stack overflow
- Tail recursion

### Examples:
```python
# Factorial using recursion
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5))

# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(10):
    print(fibonacci(i))
```

### Best Practices:
1. Always have a base case
2. Ensure the recursive case moves toward the base case
3. Be mindful of stack overflow with deep recursion
4. Consider using iteration for better performance
5. Use tail recursion when possible 