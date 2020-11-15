from asymmetric_encryption import goldwasser
import random
from prime_gen_test import eratosthenes,miller_rabin
from utils import bcolors


def check_goldwasser():
    prime_numbers = eratosthenes.gen_prime(500)

    p, q = 0, 0
    p_done = False
    q_done = False

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
    bits=10
    msg='Hello, we are testing Blum Goldwasser encryption'
    m=goldwasser.to_bits(msg)
    a=1
    b=1
    _,a,b=goldwasser.xgcd(p,q)
    r= random.getrandbits(bits)
    x0 = (a*p*r + b*q+r) % (p*q)
    c, xt = goldwasser.BGW_enc(p, q, x0, m)
    print(bcolors.OKGREEN+"\nParameters chosen:",bcolors.ENDC)
    print(("p= %d" % p))
    print(("q= %d" % q))
    print(("a= %d" % a))
    print(("b= %d" % b))
    print(("r= %d" % r))
    print(("x0= %d" % x0))
    print(("ap+bq: %d" % (a*p+b*q)))

    print(bcolors.OKBLUE+"\nCiphertext:",bcolors.ENDC, c)

    d = goldwasser.BGW_dec(p, q, a, b, xt, c)
        
    print(bcolors.OKBLUE+"Decrypted message:",bcolors.ENDC ,goldwasser.from_bits(d))


check_goldwasser()