import os
import sys
import string
import random


def convertBin(msg):
    arr = []
    for i in range(0, len(msg)):
        arr.append(int(msg[i]))

    return arr

# generate a random key of length p


def rand_key(p):
    key1 = ""
    for i in range(p):
        temp = str(random.randint(0, 1))
        key1 += temp

    return(key1)

# function to encode the messagee using the key


def enc(msg, key):
    codedKey = ''
    msg = convertBin(msg)
    key = convertBin(key)

    for i in range(0, len(msg)):
        code = (msg[i]+key[i]) % 2
        codedKey += str(code)

    return codedKey

# function to decode the coded message using the key


def dec(codedKey, key):
    codedKey = convertBin(codedKey)
    key = convertBin(key)
    msg = ''

    for i in range(0, len(codedKey)):
        txt = (codedKey[i]+key[i]) % 2
        msg += str(txt)

    return msg

# generate random numbers using LCG generator
def LCG(seed, n, a=1140671485, c=128201163, m=2**24):
    numbers = []
    for i in range(n):
        seed = (a * seed + c) % m
        numbers.append(seed)

    return numbers

# main function which is called from the test file
# it needs msg as the message to be encrypted or decrypted with option being 'd' or 'e


def main(msg, option):
    # list of options ie 'd' for decryption and 'e' for encryption
    availableOpt = ["d", "e"]

    if option == availableOpt[1]:
        rand = random.randint(1, 10000000)
        key = LCG(rand, 1)[0]
        print('key is ', key)
        binkey = bin(key)[2:]
        print('bin key is ', binkey, ' type is ', type(binkey))
        print('length of key is {} and msg is {}'.format(len(binkey), len(msg)))

        # to make the size of key as long as the message for proper XOR operation
        lkey = len(binkey)
        lmsg = len(msg)
        # quotient and remainder which can be useful to determine the remaining size of key
        quo = lmsg / lkey
        rem = lmsg % lkey

        print('quo is {} and rem is {}'.format(int(quo), rem))

        fkey = ''
        for i in range(int(quo)):
            fkey += binkey
        # final key for encryption
        fkey += binkey[:rem]
        print('final keyy is {} and its length is {} '.format(fkey, len(fkey)))
        print('msg is ', msg)
        print('key is ', key)
        print('encrypted msg is: ', enc(msg, fkey))
    elif option == availableOpt[0]:
        '''if you choose decryption, you have to provide the encrypted message
         and the key used for encryption
         msg = input("Enter the received msg: ")'''
        key = input("Enter the key used: ")
        print('original msg is: ', dec(msg, key))
