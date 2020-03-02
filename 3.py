a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
lessThanFive = len(a) - 5
b = a[0:lessThanFive]
print(b)
num = int(input("Enter number to find Min"))
for x in a:
    if x < num:
        print(x)
