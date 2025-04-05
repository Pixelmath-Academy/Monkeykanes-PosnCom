student = {
    "name": "John",
    "age": 20,
    "grades": [85, 90, 88]
}
print(student)
print(student["name"])
print(student.get("age"))
print(student.get("address", "Not found"))

student["address"] = "123 Main St"
print(student)

del student["age"]
print(student)

for key in student:
    print(key, student[key])

for key, value in student.items():
    print(key, value)

grades = student["grades"]
print(sum(grades) / len(grades))

students = {
    "John": {"age": 20, "grade": "A"},
    "Alice": {"age": 19, "grade": "B"}
}
print(students)
print(students["John"]["grade"]) 