# -*- coding: utf-8 -*-
"""
Goldwasser encryption
"""

import numpy as np
import binascii
import sys
import random

def xgcd(a, b):
    """return (g, x, y) such that a*x + b*y = g = gcd(a, b)"""
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0



# Method from https://stackoverflow.com/questions/7396849/convert-binary-to-ascii-and-vice-versa
def to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int(binascii.hexlify(text.encode(encoding, errors)), 16))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def from_bits(bits, encoding='utf-8', errors='surrogatepass'):
    n = int(bits, 2)
    return int2bytes(n).decode(encoding, errors)

def int2bytes(i):
    hex_string = '%x' % i
    n = len(hex_string)
    return binascii.unhexlify(hex_string.zfill(n + (n & 1)))

# Derived from https://github.com/coenvalk/blum-goldwasser-probabilistic-encryption/blob/master/blumgoldwasser.py
def BGW_enc(p, q, x, m):
    n = p * q


    # assert p%4 == 3 and q%4 == 4

    k = int(np.log2(n))
    h = int(np.log2(k))

    t = len(m) // h

    xi = x
    c = ''
    for i in range(t):
        mi = m[i*h:(i + 1)*h]
        xi = (xi ** 2) % n
        xi_bin = bin(xi)
        pi = xi_bin[-h:]

        mi_int = int(mi, 2)
        pi_int = int(pi, 2)

        ci = pi_int ^ mi_int
        ci_bin = format(ci, '0' + str(h) + 'b')
        c += ci_bin

    xt = (xi ** 2) % n
    return c, xt
        
    

def BGW_dec(p, q, a, b, xt, c):
    assert a*p + b*q == 1
    n=p*q
    k = int(np.log2(n))
    h = int(np.log2(k))

    t = len(c) // h

    d1 = pow((p + 1) // 4,(t + 1) , (p - 1))
    d2 = pow((q + 1) // 4,(t + 1) , (q - 1))

  #  d2 = (((q + 1) // 4)**(t + 1)) % (q - 1)

    u = pow(xt,d1,p)
    v = pow(xt,d2, q)

    x0 = (v*a*p + u*b*q) % n

    xi = x0
    m = ''
    for i in range(t):

        ci = c[i*h:(i + 1)*h]
        xi = (xi**2) % n
        xi_bin = bin(xi)
        pi = xi_bin[-h:]
        ci_int = int(ci, 2)
        pi_int = int(pi, 2)

        mi = pi_int ^ ci_int
        mi_bin = format(mi, '0' + str(h) + 'b')
        m += mi_bin

    return m

p = 523
q = 547
bits=10
msg='Hello studpid boy. You are a foll'

# if (len(sys.argv)>1):
#         bits=int(sys.argv[1])
# if (len(sys.argv)>2):
#         msg=(sys.argv[2])

m=to_bits(msg)

    

a=1
b=1

_,a,b=xgcd(p,q)


r= random.getrandbits(bits)

x0 = (a*p*r + b*q+r) % (p*q)

c, xt = BGW_enc(p, q, x0, m)

print(("Message: %s" % msg))
print(("   %s" % m))
print(("\nNo of bits in prime is %d" % bits))
print(("p= %d" % p))
print(("q= %d" % q))
print(("a= %d" % a))
print(("b= %d" % b))
print(("r= %d" % r))
print(("x0= %d" % x0))
print(("ap+bq: %d" % (a*p+b*q)))

print("\nCiphertext:", c)

d = BGW_dec(p, q, a, b, xt, c)
    
print(("Decrypted: %s" % from_bits(d)))

