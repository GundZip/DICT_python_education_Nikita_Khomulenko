import random
your_input = input("Enter size of matrix:\n> ")
cons = input("Enter constant:\n> ")
n = int(your_input[0])
m = int(your_input[2])
a = [[random.randrange(0, 10) for w in range(m)] for e in range(n)]

print(your_input)

p = 0
for i in range(n):
    for x in a[p]:
        print(x, end=" ")
    print()
    p += 1

print(cons)
print("Result:")
print()

p = 0
for i in range(n):
    k = 0
    for x in a[p]:
        x *= int(cons)
        print(x, end="  ")
        k += 1
    print()
    p += 1