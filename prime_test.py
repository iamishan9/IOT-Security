from prime_gen_test import eratosthenes, miller_rabin,fermatPrimalityCheck
from random_generators import bbs,lcg
import random
import sympy as sp
import time


prime_numbers = eratosthenes.gen_prime(10, 0)
print(prime_numbers)
p, q = 0, 0
p_done = False
# q_done = False

for i in reversed(prime_numbers):
    if not miller_rabin.millerRabin(i):
        if not(p_done):
            if i%4==3:
                p=i
                p_done= True
        else:
            if i%4==3:
                q=i
                break

print('p is {} and q is {}'.format(p, q))

bbs_number = bbs.BBS(286, 100, 200)
gen = bbs_number.Generator()
print('Rand no       Fermat check   Miller Rabin check  isPrime check')
for _ in range(0,10):
    time.sleep(0.1)
    seed=lcg.TimeSeed()
    random_number = seed.generate_seed()
    # Get number after decimal point of seed because these are the numbers that actually vary
    random_number = random_number % 1
    random_number=str(random_number)
    # Check if the number is decimal first
    if random_number.find('.') != -1:
        random_number = random_number.split('.')[1]
    # Do not split if no decimal point and just take the integer as it is
    random_number = int(random_number)
    x = lcg.LCG(random_number, 1)[0]
    print('{}    \t{} \t\t {} \t\t {}'.format(x,not(miller_rabin.millerRabin(x)),fermatPrimalityCheck.fermatPrimeCheck(x), sp.isprime(x)))