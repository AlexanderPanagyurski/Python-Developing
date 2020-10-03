n = int(input())
for x in range(n):
    print("*", end="")
print()

for x in range(1, n - 1):
    print("*", end="")
    for y in range(1, n - 1):
        print(" ", end="")
    print("*", end="")
    print()

for x in range(n):
    print("*", end="")
print()