for i in range(10):
    if i == 5:
        break
    print(i)
print("Loop ended with break")

for i in range(5):
    if i == 2:
        continue
    print(i)
print("Loop ended with continue")

for i in range(5):
    print(i)
else:
    print("Loop completed normally")

for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("This will not be printed")

found = False
for i in range(10):
    if i == 5:
        found = True
        break
if not found:
    print("Number 5 not found")

for i in range(3):
    for j in range(3):
        if i == 1 and j == 1:
            break
        print(f"i={i}, j={j}")
    if i == 1:
        break 