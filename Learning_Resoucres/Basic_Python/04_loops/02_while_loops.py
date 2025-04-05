count = 0
while count < 5:
    print(count)
    count += 1

number = 1
while number <= 10:
    if number % 2 == 0:
        print(number)
    number += 1

sum = 0
i = 1
while i <= 5:
    sum += i
    i += 1
print(f"Sum of numbers 1 to 5: {sum}")

password = "secret"
attempts = 0
while attempts < 3:
    user_input = input("Enter password: ")
    if user_input == password:
        print("Access granted!")
        break
    attempts += 1
    print(f"Wrong password. {3-attempts} attempts remaining.")

i = 0
while i < 10:
    if i == 5:
        i += 1
        continue
    print(i)
    i += 1 