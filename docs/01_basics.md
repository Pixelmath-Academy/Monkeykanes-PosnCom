# Python Basics

This section covers the fundamental concepts of Python programming.

## Contents

1. [Variables and Data Types](#variables-and-data-types)
2. [Operators](#operators)
3. [Input and Output](#input-and-output)
4. [Conditional Statements](#conditional-statements)
5. [Loops](#loops)

## Variables and Data Types

File: `01_basics/01_variables_and_data_types.py`

This file demonstrates:
- Number types (int, float)
- String type
- Boolean type
- Type conversion

### Examples:
```python
# Numbers
x = 10          # Integer
y = 3.14        # Float

# Strings
name = "Python"
message = 'Hello, World!'

# Boolean
is_true = True
is_false = False

# Type conversion
num_str = "123"
num_int = int(num_str)
num_float = float(num_str)
```

## Operators

File: `01_basics/02_operators.py`

This file covers:
- Arithmetic operators (+, -, *, /, //, %, **)
- Comparison operators (==, !=, >, <, >=, <=)
- Logical operators (and, or, not)

### Examples:
```python
# Arithmetic
a = 10
b = 3
print(a + b)    # Addition
print(a - b)    # Subtraction
print(a * b)    # Multiplication
print(a / b)    # Division
print(a // b)   # Floor division
print(a % b)    # Modulus
print(a ** b)   # Exponentiation

# Comparison
x = 5
y = 5
print(x == y)   # Equal to
print(x != y)   # Not equal to
print(x > y)    # Greater than
print(x < y)    # Less than
print(x >= y)   # Greater than or equal to
print(x <= y)   # Less than or equal to

# Logical
p = True
q = False
print(p and q)  # Logical AND
print(p or q)   # Logical OR
print(not p)    # Logical NOT
```

## Input and Output

File: `01_basics/03_input_output.py`

This file demonstrates:
- Using input() function
- Different ways to use print()
- String formatting

### Examples:
```python
# Basic input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in meters: "))

# Different print formats
print("Hello, " + name)
print(f"You are {age} years old")
print("The sum of {} and {} is {}".format(x, y, x + y))
```

## Conditional Statements

File: `01_basics/04_conditionals.py`

This file covers:
- if statements
- elif statements
- else statements
- Nested conditionals

### Examples:
```python
# Basic if-elif-else
if age < 13:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 60:
    print("You are an adult")
else:
    print("You are a senior")

# Grade calculation
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
```

## Loops

File: `01_basics/05_loops.py`

This file demonstrates:
- for loops
- while loops
- break and continue statements

### Examples:
```python
# For loop
for i in range(5):
    print(i)

# While loop
count = 0
while count < 5:
    print(count)
    count += 1

# Break statement
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue statement
for i in range(5):
    if i == 2:
        continue
    print(i)
``` 