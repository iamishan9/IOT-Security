# def bsd_rand(seed):
#     def rand():
#         nonlocal seed
#         seed = (1103515245*seed + 12345) & 0x7fffffff
#         return seed
#     return rand

# def msvcrt_rand(seed):
#     def rand():
#         nonlocal seed
#         seed = (214013*seed + 2531011) & 0x7fffffff
#         return seed >> 16
#     return rand

# print(bsd_rand(2), ' and ', msvcrt_rand(2))

# def seedLCG(initVal):
#     global rand
#     rand = initVal

# def lcg():
#     a = 1664525
#     c = 1013904223
#     m = 2**24
#     global rand
#     rand = (a*rand + c) % m
#     return rand

# seedLCG(1)

# for i in range(10):
#     print(lcg())

# import random2
# import time
# class Seed(object):
#     # Function that generates seed
#     def generate_seed(self):
#         pass


# class TimeSeed(Seed):
#     """ Generates seed from current time """
#     def generate_seed(self):
#         return time.time()

import time
import math
import numpy as np
import scipy.stats as st


class Seed(object):
    # Function that generates seed
    def generate_seed(self):
        pass


class TimeSeed(Seed):
    """ Generates seed from current time """

    def generate_seed(self):
        return time.time()


def LCG(seed, n, a=1140671485, c=128201163, m=2**24):
    numbers = []
    for i in range(n):
        seed = (a * seed + c) % m
        numbers.append(seed)

    return numbers


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

# Assuming number of runs greater than 10


# def runs_test(d, v, alpha=0.05):
#     # Get positive and negative values
#     mask = d > v
#     # get runs mask
#     p = mask == True
#     n = mask == False
#     xor = np.logical_xor(p[:-1], p[1:])
#     # A run can be identified by positive
#     # to negative (or vice versa) changes
#     d = sum(xor) + 1  # Get number of runs

#     n_p = sum(p)  # Number of positives
#     n_n = sum(n)
#     # Temporary intermediate values
#     tmp = 2 * n_p * n_n
#     tmps = n_p + n_n
#     # Expected value
#     r_hat = np.float64(tmp) / tmps + 1
#     # Variance
#     s_r_squared = (tmp*(tmp - tmps)) / (tmps*tmps*(tmps-1))
#     # Standard deviation
#     s_r = np.sqrt(s_r_squared)
#     # Test score
#     z = (d - r_hat) / s_r

#     # Get normal table
#     z_alpha = st.norm.ppf(1-alpha)
#     # Check hypothesis
#     return z, z_alpha

def random_test(list, med):
    n = len(list)
    odd = 0
    even = 0

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


    # print("Percentage of random numbers")
    # print("Total       Even         Odd")
    # print('{}           {}         {}'.format(n, even, odd))

    return even, odd, g_med, l_med


def convertBin(msg):
    arr = []
    for i in range(0, len(msg)):
        arr.append(int(msg[i]))

    return arr


def enc(msg, key):
    codedKey = ''
    msg = convertBin(msg)
    key = convertBin(key)

    for i in range(0, len(msg)):
        code = (msg[i]+key[i]) % 2
        codedKey += str(code)

    return codedKey


def dec(codedKey, key):
    codedKey = convertBin(codedKey)
    key = convertBin(key)
    msg = ''

    for i in range(0, len(codedKey)):
        txt = (codedKey[i]+key[i]) % 2
        msg += str(txt)

    return msg

# rand = random2.randint(1, 10000000)
# # rand *= 1000000
# print('rand is ', rand)
# print(LCG(rand, 1))


# def generate_lcg( num_iterations ):
#     """
#     LCG – generates as many random numbers as requested by user, using a Linear Congruential Generator
#     LCG uses the formula: X_(i+1) = (aX_i + c) mod m
#     :param num_iterations: int – the number of random numbers requested
#     :return: void
#     """
#     # Initialize variables
#     x_value = 123456789.0    # Our seed, or X_0 = 123456789
#     a = 101427               # Our "a" base value
#     c = 321                  # Our "c" base value
#     m = (2 ** 16)            # Our "m" base value

#     # counter for how many iterations we've run
#     counter = 0

#     # Open a file for output
#     outFile = open("lgc_output.txt", "wb")

#     #Perfom number of iterations requested by user
#     while counter < num_iterations:
#         # Store value of each iteration
#         x_value = (a * x_value + c) % m

#         #Obtain each number in U[0,1) by diving X_i by m
#         writeValue = str(x_value/m)

#         # write to output file
#         outFile.write(writeValue + "\n")
#         # print "num: " + " " + str(counter) +":: " + str(x_value)

#         counter = counter+1

#     outFile.close()
#     print("Successfully stored " + str(num_iterations) + " random numbers in file named: 'lgc_output.txt'.")
