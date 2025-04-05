# Python Data Structures

This section covers the fundamental data structures in Python.

## Contents

1. [Lists](#lists)
2. [Strings](#strings)
3. [Tuples and Sets](#tuples-and-sets)
4. [Dictionaries](#dictionaries)

## Lists

File: `02_data_structures/01_lists.py`

Lists are ordered, mutable sequences of elements.

### Key Features:
- Ordered collection of items
- Mutable (can be modified)
- Can contain elements of different types
- Indexed access (zero-based)

### Examples:
```python
# Creating lists
numbers = [1, 2, 3, 4, 5]

# Accessing elements
print(numbers[0])      # First element
print(numbers[-1])     # Last element
print(numbers[1:4])    # Slicing

# Modifying lists
numbers.append(6)      # Add to end
numbers.insert(0, 0)   # Insert at position
numbers.remove(3)      # Remove element
popped = numbers.pop() # Remove and return last element

# List operations
numbers.sort()         # Sort in place
numbers.reverse()      # Reverse in place
print(len(numbers))    # Get length
print(sum(numbers))    # Sum elements

# List comprehension
squares = [x**2 for x in range(5)]
```

## Strings

File: `02_data_structures/02_strings.py`

Strings are immutable sequences of characters.

### Key Features:
- Immutable (cannot be modified)
- Sequence of characters
- Rich set of methods for manipulation

### Examples:
```python
# String creation and basic operations
text = "Hello, Python!"
print(text.upper())    # Convert to uppercase
print(text.lower())    # Convert to lowercase
print(text.replace("Python", "World"))

# String methods
print(len(text))       # Get length
print("Python" in text) # Check substring
print(text.find("Python")) # Find position

# String formatting
name = "John"
age = 30
print(f"Name: {name}, Age: {age}")
print("Name: {}, Age: {}".format(name, age))

# String methods
text2 = "   spaces   "
print(text2.strip())   # Remove whitespace
print(text2.lstrip())  # Remove left whitespace
print(text2.rstrip())  # Remove right whitespace
```

## Tuples and Sets

File: `02_data_structures/03_tuples_and_sets.py`

### Tuples
- Immutable sequences
- Ordered collection
- Can contain elements of different types

### Examples:
```python
# Tuple creation and usage
point = (3, 4)
x, y = point  # Unpacking

coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"Point: ({x}, {y})")
```

### Sets
- Unordered collection of unique elements
- Mutable
- No duplicates allowed

### Examples:
```python
# Set operations
numbers = {1, 2, 3, 3, 4, 4, 5}  # Duplicates removed
numbers.add(6)                    # Add element
numbers.remove(3)                 # Remove element

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))          # Union
print(set1.intersection(set2))   # Intersection
print(set1.difference(set2))     # Difference
```

## Dictionaries

File: `02_data_structures/04_dictionaries.py`

Dictionaries are key-value pairs.

### Key Features:
- Unordered collection
- Key-value pairs
- Keys must be unique
- Mutable

### Examples:
```python
# Dictionary creation and access
student = {
    "name": "John",
    "age": 20,
    "grades": [85, 90, 88]
}

# Accessing values
print(student["name"])
print(student.get("age"))
print(student.get("address", "Not found"))

# Modifying dictionaries
student["address"] = "123 Main St"
del student["age"]

# Iterating over dictionaries
for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, value)

# Nested dictionaries
students = {
    "John": {"age": 20, "grade": "A"},
    "Alice": {"age": 19, "grade": "B"}
}
``` 