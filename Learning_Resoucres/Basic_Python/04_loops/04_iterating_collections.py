fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

numbers = [1, 2, 3, 4, 5]
for num in numbers:
    print(num * 2)

for i in range(len(numbers)):
    print(f"Index {i}: {numbers[i]}")

person = {"name": "John", "age": 30, "city": "New York"}
for key in person:
    print(key)

for value in person.values():
    print(value)

for key, value in person.items():
    print(f"{key}: {value}")

text = "Python"
for char in text:
    print(char)

for i, char in enumerate(text):
    print(f"Position {i}: {char}")

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
for row in matrix:
    for cell in row:
        print(cell, end=" ")
    print() 