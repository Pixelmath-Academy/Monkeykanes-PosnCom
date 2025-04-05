squares = [x**2 for x in range(5)]
print(squares)

even_numbers = [x for x in range(10) if x % 2 == 0]
print(even_numbers)

words = ["hello", "world", "python"]
upper_words = [word.upper() for word in words]
print(upper_words)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [cell for row in matrix for cell in row]
print(flattened)

squares_gen = (x**2 for x in range(5))
for square in squares_gen:
    print(square)

even_gen = (x for x in range(10) if x % 2 == 0)
for even in even_gen:
    print(even)

words = ["hello", "world", "python"]
lengths = {word: len(word) for word in words}
print(lengths)

numbers = [1, 2, 3, 4, 5]
doubled = {x: x*2 for x in numbers}
print(doubled)

unique_lengths = {len(word) for word in words}
print(unique_lengths) 