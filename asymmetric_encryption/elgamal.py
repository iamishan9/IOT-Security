# -*- coding: utf-8 -*-
"""
Elgamal encryption
"""

import random
import math
import sys

# class for public key


class PublicKey(object):
    def __init__(self, p=None, g=None, A=None, numBits=0):
        self.p = p
        self.g = g
        self.A = A
        self.numBits = numBits

# class for Private Key


class PrivateKey(object):
    def __init__(self, x=None, numBits=0):
        self.x = x
        self.numBits = numBits

# computes base^exp mod modulus


def modexp(base, exp, modulus):
    return pow(base, exp, modulus)

# computes the greatest common denominator of a and b.  assumes a > b


def gcd(x, y):
    while(y):
        x, y = y, x % y
    return x

# find n bit prime


def generate_prime(numBits, confidence):
    # keep testing until 1 is returned
    while(1):
        # generate potential prime number randomly
        p = random.randint(2**(numBits-2), 2**(numBits-1))
        # check if it is odd
        while(p % 2 == 0):
            p = random.randint(2**(numBits-2), 2**(numBits-1))

        # pass through the solovay strassen primality checker
        while(not solovay_strassen(p, confidence)):
            p = random.randint(2**(numBits-2), 2**(numBits-1))
            while(p % 2 == 0):
                p = random.randint(2**(numBits-2), 2**(numBits-1))

        # if p is prime compute p = 2*p + 1
        # if p is prime, we have succeeded; else, start over
        p = p * 2 + 1
        if solovay_strassen(p, confidence):
            return p


def find_primitive_root(p):
    if p == 2:
        return 1
    # the prime divisors of p-1 are 2 and (p-1)/2 because
    # p = 2x + 1 where x is a prime
    p1 = 2
    p2 = (p-1) // p1

    # test random g's until one is found that is a primitive root mod p
    while(1):
        g = random.randint(2, p-1)
        # g is a primitive root if for all prime factors of p-1, p[i]
        # g^((p-1)/p[i]) (mod p) is not congruent to 1
        if not (modexp(g, (p-1)//p1, p) == 1):
            if not modexp(g, (p-1)//p2, p) == 1:
                return g

# encodes bytes to integers mod p.  reads bytes from file


def encode(sPlaintext, numBits):
    byte_array = bytearray(sPlaintext, 'utf-16')

    # z is the array of integers mod p
    z = []

    # each encoded integer will be a linear combination of k message bytes
    # k must be the number of bits in the prime divided by 8 because each
    # message byte is 8 bits long
    k = numBits//8

    # j marks the jth encoded integer
    # j will start at 0 but make it -k because j will be incremented during first iteration
    j = -1 * k
    # num is the summation of the message bytes
    num = 0
    # i iterates through byte array
    for i in range(len(byte_array)):
        # if i is divisible by k, start a new encoded integer
        if i % k == 0:
            j += k
            num = 0
            z.append(0)
        # add the byte multiplied by 2 raised to a multiple of 8
        z[j//k] += byte_array[i]*(2**(8*(i % k)))

    # example
        # if n = 24, k = n / 8 = 3
        # z[0] = (summation from i = 0 to i = k)m[i]*(2^(8*i))
        # where m[i] is the ith message byte

    # return array of encoded integers
    return z


# decodes integers to the original message bytes
def decode(aiPlaintext, numBits):
    # bytes array will hold the decoded original message bytes
    bytes_array = []

    # same deal as in the encode function.
    # each encoded integer is a linear combination of k message bytes
    # k must be the number of bits in the prime divided by 8 because each
    # message byte is 8 bits long
    k = numBits//8

    # num is an integer in list aiPlaintext
    for num in aiPlaintext:
        # get the k message bytes from the integer, i counts from 0 to k-1
        for i in range(k):
            # temporary integer
            temp = num
            # j goes from i+1 to k-1
            for j in range(i+1, k):
                # get remainder from dividing integer by 2^(8*j)
                temp = temp % (2**(8*j))
            # message byte representing a letter is equal to temp divided by 2^(8*i)
            letter = temp // (2**(8*i))
            # add the message byte letter to the byte array
            bytes_array.append(letter)
            # subtract the letter multiplied by the power of two from num so
            # so the next message byte can be found
            num = num - (letter*(2**(8*i)))

    # example
    # if "You" were encoded.
    # Letter        #ASCII
    # Y              89
    # o              111
    # u              117
    # if the encoded integer is 7696217 and k = 3
    # m[0] = 7696217 % 256 % 65536 / (2^(8*0)) = 89 = 'Y'
    # 7696217 - (89 * (2^(8*0))) = 7696128
    # m[1] = 7696128 % 65536 / (2^(8*1)) = 111 = 'o'
    # 7696128 - (111 * (2^(8*1))) = 7667712
    # m[2] = 7667712 / (2^(8*2)) = 117 = 'u'

    decodedText = bytearray(b for b in bytes_array).decode('utf-16')

    return decodedText


# Solovay strassen primality test function

def solovay_strassen(num, num_iterations):
    # ensure confidence of num_iterations interations
    for i in range(num_iterations):
        # choose random a between 1 and n-2
        a = random.randint(1, num-1)

        # if a is not relatively prime to n, n is composite
        if gcd(a, num) > 1:
            return False

        # declares n prime if jacobi(a, n) is congruent to a^((n-1)/2) mod n
        if not calculateJacobian(a, num) % num == modexp(a, (num-1)//2, num):
            return False

    # if there have been num_iterations iterations without failure, num is believed to be prime
    return True

# computes the jacobi symbol of a, n
# To calculate Jacobian symbol of a
# given number


def calculateJacobian(a, n):

    if (a == 0):
        return 0  # (0/n) = 0

    ans = 1
    if (a < 0):

        # (a/n) = (-a/n)*(-1/n)
        a = -a
        if (n % 4 == 3):

            # (-1/n) = -1 if n = 3 (mod 4)
            ans = -ans

    if (a == 1):
        return ans  # (1/n) = 1

    while (a):
        if (a < 0):

            # (a/n) = (-a/n)*(-1/n)
            a = -a
            if (n % 4 == 3):

                # (-1/n) = -1 if n = 3 (mod 4)
                ans = -ans

        while (a % 2 == 0):
            a = a // 2
            if (n % 8 == 3 or n % 8 == 5):
                ans = -ans

        # swap
        a, n = n, a

        if (a % 4 == 3 and n % 4 == 3):
            ans = -ans
        a = a % n

        if (a > n // 2):
            a = a - n

    if (n == 1):
        return ans

    return 0


def generate_keys(numBits=256, confidence=32):
                # p is the prime
                # g is the primitve root
                # a is random in (0, p-1) inclusive
                # A = g ^ x mod p
    p = generate_prime(numBits, confidence)
    g = find_primitive_root(p)
    g = modexp(g, 2, p)
    a = random.randint(1, (p - 1) // 2)
    A = modexp(g, a, p)

    publicKey = PublicKey(p, g, A, numBits)
    privateKey = PrivateKey(a, numBits)

    return {'privateKey': privateKey, 'publicKey': publicKey}

# encrypts a string sPlaintext using the public key k


def digit(key, sPlaintext):
    z = encode(sPlaintext, key.numBits)

    # cipher_pairs list will hold pairs (c, d) corresponding to each integer in z
    cipher_pairs = []
    # i is an integer in z
    for i in z:
        # pick random y from (0, p-1) inclusive
        y = random.randint(0, key.p)
        # c = g^y mod p
        c = modexp(key.g, y, key.p)
        # d = ih^y mod p
        d = (i*modexp(key.A, y, key.p)) % key.p
        # add the pair to the cipher pairs list
        cipher_pairs.append([c, d])

    encryptedStr = ""
    for pair in cipher_pairs:
        encryptedStr += str(pair[0]) + ' ' + str(pair[1]) + ' '

    return encryptedStr

# performs decryption on the cipher pairs found in Cipher using
# prive key K2 and writes the decrypted values to file Plaintext


def decipher(priv, pub, cipher):
    # decrpyts each pair and adds the decrypted integer to list of plaintext integers
    plaintext = []

    cipherArray = cipher.split()
    if (not len(cipherArray) % 2 == 0):
        return "Malformed Cipher Text"
    for i in range(0, len(cipherArray), 2):
        # c = first number in pair
        c = int(cipherArray[i])
        # d = second number in pair
        d = int(cipherArray[i+1])

        # s = c^x mod p
        s = modexp(c, priv.x, pub.p)
        # plaintext integer = ds^-1 mod p
        plain = (d*modexp(s, pub.p-2, pub.p)) % pub.p
        # add plain to list of plaintext integers
        plaintext.append(plain)

    decryptedText = decode(plaintext, pub.numBits)

    # remove trailing null bytes
    decryptedText = "".join([ch for ch in decryptedText if ch != '\x00'])

    return decryptedText




# keys = None
# cipher = None

# while True:
#     value = input(
#         "Choose 1 for generating key, 2 for encrypting message, 3 for decrypting message, 4 for quitting the program.:\n")
#     if value == "1":
#         keys = generate_keys()
#         priv = keys['privateKey']
#         pub = keys['publicKey']
#         cipher = None
#     elif value == "2":
#         if keys is None:
#             print("Generate key first.\n")
#             continue
#         else:
#             message = input("Enter message:")
#             cipher = digit(pub, str(message))
#             print("Message encrypted\n")

#     elif value == "3":
#         if cipher is None:
#             print("No message encrypted. Encrypt first\n")
#         else:
#             decrypted_message = decipher(priv, pub, cipher)
#             print("The message received is:", decrypted_message, "\n")
#     else:
#         break
