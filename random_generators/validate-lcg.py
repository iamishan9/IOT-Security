import math
'''
contains functions which allow us to validate lcg
'''



def gcd(x, y):

    while(y):
        x, y = y, x % y

    return x


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def is_coprime(x, y):
    return gcd(x, y) == 1


def parameters_check_lcg(a, c, m):
    suitable = True
    if c == 0:
        suitable = False
    if not is_coprime(c, m):
        suitable = False
    p = prime_factors(m)
    for i in p:
        if not (a-1) % i == 0:
            suitable = False
            break

    if m % 4 == 0:
        if not (a-1) % 4 == 0:
            suitable = False

    return suitable


print(parameters_check_lcg(1140671485, 128201163, 2**24))
