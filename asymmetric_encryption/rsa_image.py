'''
Encryption and decryption of an image using RSA
'''
# importing all libraries
import cv2
import numpy as np
from skimage import io
import matplotlib.pyplot as plt
from random import randrange, getrandbits

# modular power
def power(a, d, n):
    ans = 1
    while d != 0:
        if d % 2 == 1:
            ans = ((ans % n)*(a % n)) % n
        a = ((a % n)*(a % n)) % n
        d >>= 1
    return ans

# miller rabin to check primality
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


# check if number is prime
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
        # calling Miller rabin
        if not MillerRabin(N, d):
            return False
    return True

# generating prime candidate
def generate_prime_candidate(length):
    # generate random bits
    p = getrandbits(length)
    p |= (1 << length - 1) | 1
    return p

# generating prime number
def generatePrimeNumber(length):
    A = 4
    while not is_prime(A, 128):
        A = generate_prime_candidate(length)
    return A

# function that starts encryption called from test file
def start():

    # path of image file to be encrypted
    my_img = io.imread('./asymmetric_encryption/image.jpg')

    # height and width of image
    height, width = my_img.shape[0], my_img.shape[1]
    print('height is {} and width is {}'.format(height, width))

    # generating P and Q
    length = 5
    P = generatePrimeNumber(length)
    Q = generatePrimeNumber(length)

    # printing them
    print(P)
    print(Q)


    # Calculating N=P*Q and Euler Totient Function = (P-1)*(Q-1)
    N = P*Q
    eulerTotient = (P-1)*(Q-1)
    print(N)
    print(eulerTotient)


    # Step 3: Find E such that GCD(E,eulerTotient)=1
    # (i.e., e should be co-prime) such that it satisfies this condition:- 
    #  1<E<eulerTotient

    def GCD(a, b):
        if a == 0:
            return b
        return GCD(b % a, a)


    E = generatePrimeNumber(4)
    while GCD(E, eulerTotient) != 1:
        E = generatePrimeNumber(4)
    print(E)


    # Find D.
    def gcdExtended(E, eulerTotient):
        a1, a2, b1, b2, d1, d2 = 1, 0, 0, 1, eulerTotient, E

        while d2 != 1:

            # k
            k = (d1//d2)

            # a
            temp = a2
            a2 = a1-(a2*k)
            a1 = temp

            # b
            temp = b2
            b2 = b1-(b2*k)
            b1 = temp

            # d
            temp = d2
            d2 = d1-(d2*k)
            d1 = temp

            D = b2

        if D > eulerTotient:
            D = D % eulerTotient
        elif D < 0:
            D = D+eulerTotient

        return D


    D = gcdExtended(E, eulerTotient)
    print(D)
    row, col = my_img.shape[0], my_img.shape[1]
    enc = [[0 for x in range(3000)] for y in range(3000)]


    # Encrypting image
    for i in range(0, height):
        for j in range(0, width):
            r, g, b = my_img[i, j]
            C1 = power(r, E, N)
            C2 = power(g, E, N)
            C3 = power(b, E, N)
            enc[i][j] = [C1, C2, C3]
            C1 = C1 % 256
            C2 = C2 % 256
            C3 = C3 % 256
            my_img[i, j] = [C1, C2, C3]

    # plotting encrypted image
    fig=plt.figure()
    fig.add_subplot(1,2, 1)
    plt.xlabel('Image encryption')
    plt.imshow(my_img, cmap="gray")


    # Decrypting image
    for i in range(0, height):
        for j in range(0, width):
            r, g, b = enc[i][j]
            M1 = power(r, D, N)
            M2 = power(g, D, N)
            M3 = power(b, D, N)
            my_img[i, j] = [M1, M2, M3]

    # plotting decrypted image
    fig.add_subplot(1,2, 2)
    plt.imshow(my_img, cmap="gray")
    plt.xlabel('Image decryption')
    plt.show(block='True')
