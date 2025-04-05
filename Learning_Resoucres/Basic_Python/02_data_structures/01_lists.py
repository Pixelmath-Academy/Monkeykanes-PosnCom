numbers = [1, 2, 3, 4, 5]
print(numbers)
print(numbers[0])
print(numbers[-1])
print(numbers[1:4])
print(numbers[::2])

numbers.append(6)
print(numbers)

numbers.insert(0, 0)
print(numbers)

numbers.remove(3)
print(numbers)

popped = numbers.pop()
print(popped)
print(numbers)

numbers.sort()
print(numbers)

numbers.reverse()
print(numbers)

print(len(numbers))
print(sum(numbers))

for num in numbers:
    print(num)

squares = [x**2 for x in range(5)]
print(squares) 