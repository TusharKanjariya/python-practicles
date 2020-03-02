import random

a = list()
b = list()
for x in range(0, 9):
    a.append(random.randint(1, 100))
    if (a[x] % 2) == 0:
        b.append(a[x])

print(a)
print(b)
