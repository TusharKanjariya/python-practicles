from datetime import date

name = input("Enter Name")
age = input("Enter Age")

if age.isalpha():
    print("Enter Age Number")
else:
    final = 100 - int(age)
    current = date.today()
    print(name + "is 100 years at " + str(current.year + final))
