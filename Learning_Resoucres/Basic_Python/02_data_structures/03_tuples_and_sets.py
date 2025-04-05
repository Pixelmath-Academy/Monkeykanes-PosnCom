point = (3, 4)
print(point)
print(point[0])
print(point[1])

x, y = point
print(x, y)

coordinates = [(1, 2), (3, 4), (5, 6)]
for x, y in coordinates:
    print(f"Point: ({x}, {y})")

numbers = {1, 2, 3, 3, 4, 4, 5}
print(numbers)

numbers.add(6)
print(numbers)

numbers.remove(3)
print(numbers)

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))

frozen = frozenset([1, 2, 3])
print(frozen) 