# -*- coding: utf-8 -*-
"""
Goldwasser encryption
"""
# importing all libraries
import numpy as np
import binascii
import sys
import random

# return (g,x,y) such that a*x+b*y=g=gcd(a,b)
def xgcd(a, b):
    x0, x1, y0, y1 = 0, 1, 1, 0
    while a != 0:
        (q, a), b = divmod(b, a), a
        y0, y1 = y1, y0 - q * y1
        x0, x1 = x1, x0 - q * x1
    return b, x0, y0

# method to convert binary into ascii and vice versa
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


# function to encrypt
def BGW_enc(n, x, m):
    
    # assert p%4 == 3 and q%4 == 4
    # computing h
    k = int(np.log2(n))
    h = int(np.log2(k))

    #  convert sequence into t blocks
    t = len(m) // h
    xi = x
    c = ''

    # for i from 1 to t
    for i in range(t):
        mi = m[i*h:(i + 1)*h]
        # computing xi
        xi = (xi ** 2) % n
        xi_bin = bin(xi)

        # least significant h bits of xi
        pi = xi_bin[-h:]

        mi_int = int(mi, 2)
        pi_int = int(pi, 2)

        # xor
        ci = pi_int ^ mi_int

        # converting to bianry and concatenating
        ci_bin = format(ci, '0' + str(h) + 'b')
        c += ci_bin

    xt = (xi ** 2) % n
    return c, xt
        
    
# function to decrypt
def BGW_dec(p, q, a, b, xt, c):
    assert a*p + b*q == 1
    n=p*q
    k = int(np.log2(n))
    h = int(np.log2(k))

    t = len(c) // h

    dp = pow((p + 1) // 4,(t + 1) , (p - 1))
    dq = pow((q + 1) // 4,(t + 1) , (q - 1))

    up = pow(xt,dp,p)
    uq = pow(xt,dq, q)

    x0 = (uq*a*p + up*b*q) % n
    xi = x0

    m = ''

    # from i to t
    for i in range(t):

        ci = c[i*h:(i + 1)*h]
        xi = (xi**2) % n
        xi_bin = bin(xi)

        # least significant h bits of xi
        pi = xi_bin[-h:]
        ci_int = int(ci, 2)
        pi_int = int(pi, 2)

        # xor
        mi = pi_int ^ ci_int
        mi_bin = format(mi, '0' + str(h) + 'b')
        
        # concat message
        m += mi_bin

    return m


