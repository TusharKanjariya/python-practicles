num = int(input("Enter Number"))
print("divisior of " + str(num))
for x in range(1, num + 1):
    temp = num % x
    if (num % x) == 0:
        print(x)
