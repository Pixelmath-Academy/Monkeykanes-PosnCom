n = 5

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("--------------------------------")

for i in range(n):
    for j in range(n):
        if i == j or i + j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("--------------------------------")

for i in range(n):
    for j in range(n):
        if (i + j) % 2 == 0:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("--------------------------------")

for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1 or i == j or i + j == n-1:
            print("*", end="")
        else:
            print(" ", end="")
    print()