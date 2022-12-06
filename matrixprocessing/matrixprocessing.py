a = [[4, 5, 2, 1],
     [2, 3, 3, 1],
     [1, 1, 4, 3],
     [0, 0, 5, 5]]

b = [[0, 1, 1, 3],
     [4, 4, 1, 2],
     [3, 2, 1, 5],
     [9, 1, 6, 7]]

print("4 4")
p = 0
for i in a[p]:
    for x in a[p]:
        print(x, end="  ")
    print()
    p += 1

print("4 4")
p = 0
for i in b[p]:
    for x in b[p]:
        print(x, end="  ")
    print()
    p += 1
print("Result:")

if len(a) == len(b):
    p = 0
    for i in a[p]:
        k = 0
        for x in a[p]:
            x += b[p][k]
            print(x, end="  ")
            k += 1
        print()
        p += 1
else:
    print("ERROR")