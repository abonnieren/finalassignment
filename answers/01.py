import math

def primeChecker(n):
    if n > 1:
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
                break
        return True
    else:
        return False

num = int(input("Enter a number: "))
if primeChecker(num):
    print("Prime")
else:
    print("Not Prime")
