str1 = input("enter string")
str2 = input("enter string")

if len(str1) != len(str2):
    print("Length Not Equal")

print(tuple(zip(str1, str2)))

for x, y in zip(str1, str2):
    if x != y:
        print("Not Equal")
    else:
        print("Equal")
