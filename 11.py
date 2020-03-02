import random

x = random.randint(1, 9)
print(x)
while "true":
    userInp = input("Guess number")
    if userInp == "exit":
        break
    else:
        if int(userInp) > x:
            print("High")
        elif int(userInp) < x:
            print("Low")
        else:
            print("Done")
            break

