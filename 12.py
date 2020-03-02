num1 = int(input("Enter Number"))

for x in range(2, num1):
    if (num1 % x) == 0:
        print(str(num1) + "is not a Prime Number")
        break
    else:
        print(str(num1) + "is a Prime Number")

# With a Function


def isprime(y):
    for x in range(2, y):
        if (num1 % x) == 0:
            print(str(y) + "is not a Prime Number")
            break
        else:
            print(str(y) + "is a Prime Number")


# isprime(12)
