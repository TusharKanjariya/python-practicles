def getfactors(x):
    for y in range(1, x + 1):
        if (x % y) == 0:
            print(y)


getfactors(12)
