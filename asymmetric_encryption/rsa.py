# importing all libraries
from random import getrandbits,randrange
import sys
sys.path.append('../')
from rapid_exponentiation import exp_wo_recursion as exp

# calculating gcd
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# function to encrypt message
def encrypt(message, n, c):
    message_letters = [ord(letter) for letter in message]
    message_encrypted = ''.join([chr(exp.find_expo(letter,c)[0] % n) for letter in message_letters])
    return message_encrypted

# function to decrypt message
def decrypt(message_encrypted, n, d):
    message_encrypted_letters = [ord(letter) for letter in message_encrypted]
    message = ''.join([chr(exp.find_expo(letter,d)[0]% n) for letter in message_encrypted_letters])
    return message

# function to generate n,c and d using prime number p1 & p2
def keygen(p1, p2):
    n = p1 * p2
    
    totient = (p1 - 1) * (p2 - 1)

    public_keys = []
    for i in range(totient):
        if gcd(i, totient) == 1:
            public_keys.append(i)

    # selecting just the 5th one as public key, any could be selected
    public_key = public_keys[4]

    private_key = 0
    x = -1
    while x != 0:
        private_key += 1
        x = (public_key * private_key - 1) % totient

    return (n, public_key, private_key)

# 
def power(a, d, n):
    ans = 1
    while d != 0:
        if d % 2 == 1:
            ans = ((ans % n)*(a % n)) % n
        a = ((a % n)*(a % n)) % n
        d >>= 1
    return ans


def MillerRabin(N, d):
    a = randrange(2, N - 1)
    x = power(a, d, N)
    if x == 1 or x == N-1:
        return True
    else:
        while(d != N-1):
            x = ((x % N)*(x % N)) % N
            if x == 1:
                return False
            if x == N-1:
                return True
            d <<= 1
    return False


def is_prime(N, K):
    if N == 3 or N == 2:
        return True
    if N <= 1 or N % 2 == 0:
        return False

    # Find d such that d*(2^r)=X-1
    d = N-1
    while d % 2 != 0:
        d /= 2

    for _ in range(K):
        if not MillerRabin(N, d):
            return False
    return True


def generate_prime_candidate(length):
    # generate random bits
    p = getrandbits(length)
    p |= (1 << length - 1) | 1
    return p


def generatePrimeNumber(length):
    A = 4
    while not is_prime(A, 128):
        A = generate_prime_candidate(length)
    return A
