from random import randint
 
def fermatPrimeCheck(n, k = 5):
    if (n>9 and (n % 10 == 0 or n % 10 == 2 or n % 10 == 4 or n % 10 == 5 or n % 10 == 6 or n % 10 == 8) ):
        return False
    output = True
    for i in range(0, k):
        a = randint(1, n-1)
        if (pow(a, n-1, n) != 1):
            return False 
    return output

print(fermatPrimeCheck(102))

