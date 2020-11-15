# importing all the libraries
from prime_gen_test import eratosthenes, miller_rabin,fermatPrimalityCheck
from random_generators import bbs,lcg
import random
import sympy as sp
import time
from utils import bcolors

# Generating prime number upto 500 using eratosthens seive
print(bcolors.OKGREEN+"\n Generating prime numbers between 500 and 600 using Eratosthenes Seive:"+bcolors.ENDC)
prime_numbers = eratosthenes.gen_prime(500)
print(prime_numbers,"\n")


# Checking if number is prime using Ferman check, Miller Rabin and scipy isprime
print(bcolors.OKGREEN+'Rand no       Fermat check   Miller Rabin check  isPrime check'+bcolors.ENDC)
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