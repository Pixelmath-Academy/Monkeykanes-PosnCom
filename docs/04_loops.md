# Python Loops

This section covers different types of loops and their applications in Python.

## Contents

1. [Basic For Loops](#basic-for-loops)
2. [While Loops](#while-loops)
3. [Loop Control](#loop-control)
4. [Iterating Collections](#iterating-collections)
5. [Comprehensions](#comprehensions)

## Basic For Loops

File: `04_loops/01_basic_for_loops.py`

For loops are used to iterate over a sequence.

### Key Features:
- Iterate over range()
- Iterate over sequences
- Nested loops
- Loop variables

### Examples:
```python
# Basic range loop
for i in range(5):
    print(i)

# Range with start and stop
for i in range(2, 8):
    print(i)

# Range with step
for i in range(0, 10, 2):
    print(i)

# Nested loops
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
```

## While Loops

File: `04_loops/02_while_loops.py`

While loops continue as long as a condition is true.

### Key Features:
- Condition-based iteration
- Infinite loops
- Break and continue
- Loop control

### Examples:
```python
# Basic while loop
count = 0
while count < 5:
    print(count)
    count += 1

# While with condition
number = 1
while number <= 10:
    if number % 2 == 0:
        print(number)
    number += 1

# While with break
password = "secret"
attempts = 0
while attempts < 3:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted!")
        break
    attempts += 1
```

## Loop Control

File: `04_loops/03_loop_control.py`

Control statements modify loop behavior.

### Key Features:
- break statement
- continue statement
- else clause
- Nested loop control

### Examples:
```python
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

# Else clause
for i in range(5):
    print(i)
else:
    print("Loop completed normally")
```

## Iterating Collections

File: `04_loops/04_iterating_collections.py`

Different ways to iterate over collections.

### Key Features:
- List iteration
- Dictionary iteration
- String iteration
- enumerate() function

### Examples:
```python
# List iteration
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Dictionary iteration
person = {"name": "John", "age": 30}
for key in person:
    print(key)
for value in person.values():
    print(value)
for key, value in person.items():
    print(f"{key}: {value}")

# String iteration
text = "Python"
for char in text:
    print(char)
```

## Comprehensions

File: `04_loops/05_comprehensions.py`

Comprehensions provide concise ways to create collections.

### Key Features:
- List comprehensions
- Dictionary comprehensions
- Set comprehensions
- Generator expressions

### Examples:
```python
# List comprehension
squares = [x**2 for x in range(5)]
even_numbers = [x for x in range(10) if x % 2 == 0]

# Dictionary comprehension
words = ["hello", "world", "python"]
lengths = {word: len(word) for word in words}

# Set comprehension
unique_lengths = {len(word) for word in words}

# Generator expression
squares_gen = (x**2 for x in range(5))
for square in squares_gen:
    print(square)
``` 