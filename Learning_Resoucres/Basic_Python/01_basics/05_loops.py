for i in range(5):
    print(i)

for i in range(2, 8):
    print(i)

for i in range(0, 10, 2):
    print(i)

sum = 0
for i in range(1, 6):
    sum += i
print(f"Sum of numbers 1 to 5: {sum}")

for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i} x {j} = {i * j}")

count = 0
while count < 5:
    print(count)
    count += 1

number = 1
while number <= 10:
    if number % 2 == 0:
        print(number)
    number += 1

for i in range(10):
    if i == 5:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i) 