str1 = input("enter String")

length = len(str1)
str2 = str1[::-1]

if str1 == str2:
    print(str1 + " is Plaindrome")
else:
    print(str1 + " is not Plaindrome")
