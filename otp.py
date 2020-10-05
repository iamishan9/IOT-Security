import os
import sys
import string
import random

abc = string.ascii_lowercase
one_time_pad = list(abc)

# print('abc is ', abc)
# random.shuffle(one_time_pad)

help = """python otp.py -e|-d
-e for encryption
-d for decryption """

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    # print("Random Key of length ", length, "is:", result_str)
    return result_str

def encrypt(msg, key):
    ciphertext = ''
    for idx, char in enumerate(msg):
        charIdx = abc.index(char)
        keyIdx = one_time_pad.index(key[idx])

        cipher = (keyIdx + charIdx) % len(one_time_pad)
        ciphertext += abc[cipher]

    return ciphertext


def decrypt(ciphertext, key):
    if ciphertext == '' or key == '':
        return ''

    charIdx = abc.index(ciphertext[0])
    keyIdx = one_time_pad.index(key[0])

    cipher = (charIdx - keyIdx) % len(one_time_pad)
    char = abc[cipher]

    return char + decrypt(ciphertext[1:], key[1:])

if __name__ == '__main__':
    availableOpt = ["-d", "-e"]
    if len(sys.argv) == 1 or sys.argv[1] not in availableOpt:
        print(help)
        exit(0)

    msg = "ishan"
    key = get_random_string(len(msg))
    
    if sys.argv[1] == availableOpt[1]:
        print('msg is ', msg)
        print('key is ', key)
        print('encrypted msg is: ',encrypt(msg, key))
    elif sys.argv[1] == availableOpt[0]:
        msg = input("Enter the received msg: ")
        key = input("Enter the key used: ")
        print('original msg is: ',decrypt(msg, key))
