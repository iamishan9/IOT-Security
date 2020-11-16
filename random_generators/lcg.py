# importing all libraries
import time
import math
import numpy as np
import scipy.stats as st

# lcg random generator
def LCG(seed, n, a=1140671485, c=128201163, m=2**24):
    numbers = []
    for i in range(n):
        seed = (a * seed + c) % m
        numbers.append(seed)

    return numbers

# greatest common divisor
def gcd(x, y):

    while(y):
        x, y = y, x % y

    return x

# finding prime factors
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

# check coprime
def is_coprime(x, y):
    return gcd(x, y) == 1

# check if parameters for lcg are good
def parameters_check_lcg(a, c, m):
    suitable = True
    if c == 0:
        suitable = False
    # checking coptime
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

# checking randomness of numbers generated
def random_test(list, med):
    n = len(list)

    # odd and even percentage
    odd = 0
    even = 0

    # greater or lower than median
    g_med = 0
    l_med = 0

    for i in list:
        if i%2 == 0:
            even += 1
        else:
            odd += 1
        
        if i>=med:
            g_med += 1
        else:
            l_med +=1
    
    even = round(even/n * 100, 2)
    odd = round(odd/n * 100, 2)

    g_med = round(g_med/n * 100, 2)
    l_med = round(l_med/n * 100, 2)

    return even, odd, g_med, l_med


# convert to binary
def convertBin(msg):
    arr = []
    for i in range(0, len(msg)):
        arr.append(int(msg[i]))

    return arr

# encrypt
def enc(msg, key):
    codedKey = ''
    msg = convertBin(msg)
    key = convertBin(key)

    for i in range(0, len(msg)):
        code = (msg[i]+key[i]) % 2
        codedKey += str(code)

    return codedKey

# decrypt
def dec(codedKey, key):
    codedKey = convertBin(codedKey)
    key = convertBin(key)
    msg = ''

    for i in range(0, len(codedKey)):
        txt = (codedKey[i]+key[i]) % 2
        msg += str(txt)
    return msg
