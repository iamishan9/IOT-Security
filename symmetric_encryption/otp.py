import os
import sys
import string
import random2

# abc = string.ascii_lowercase
# one_time_pad = list(abc)

# print('abc is ', abc)
# random.shuffle(one_time_pad)

help = """python otp.py -e|-d
-e for encryption
-d for decryption """

# def get_random_string(length):
#     letters = string.ascii_lowercase
#     result_str = ''.join(random.choice(letters) for i in range(length))
#     # print("Random Key of length ", length, "is:", result_str)
#     return result_str

# def encrypt(msg, key):
#     ciphertext = ''
#     for idx, char in enumerate(msg):
#         charIdx = abc.index(char)
#         keyIdx = one_time_pad.index(key[idx])

#         cipher = (keyIdx + charIdx) % len(one_time_pad)
#         ciphertext += abc[cipher]

#     return ciphertext


# def decrypt(ciphertext, key):
#     if ciphertext == '' or key == '':
#         return ''

#     charIdx = abc.index(ciphertext[0])
#     keyIdx = one_time_pad.index(key[0])

#     cipher = (charIdx - keyIdx) % len(one_time_pad)
#     char = abc[cipher]

#     return char + decrypt(ciphertext[1:], key[1:])

def convertBin(msg):
    arr = []
    for i in range (0,len(msg)):
        arr.append(int(msg[i]))
    
    return arr

def rand_key(p): 
    
    # Variable to store the  
    # string 
    key1 = "" 

    # Loop to find the string 
    # of desired length 
    for i in range(p): 
        # randint function to generate 
        # 0, 1 randomly and converting  
        # the result into str 
        temp = str(random.randint(0, 1)) 

        # Concatenatin the random 0, 1 
        # to the final result 
        key1 += temp 

    return(key1) 


def enc(msg, key):
    codedKey = ''
    msg = convertBin(msg)
    key = convertBin(key)

    for i in range(0,len(msg)):
        code = (msg[i]+key[i])%2
        codedKey += str(code)

    return codedKey

def dec(codedKey, key):
    codedKey = convertBin(codedKey)
    key = convertBin(key)
    msg = ''

    for i in range(0,len(codedKey)):
        txt = (codedKey[i]+key[i])%2
        msg += str(txt)

    return msg

def LCG(seed, n, a= 1140671485, c=128201163, m=2**24):
    numbers = []
    for i in range(n):
        seed = (a * seed + c) % m
        numbers.append(seed)

    return numbers

if __name__ == '__main__':
    availableOpt = ["-d", "-e"]
    if len(sys.argv) == 1 or sys.argv[1] not in availableOpt:
        print(help)
        exit(0)

    # msg = "ishan"
    # key = get_random_string(len(msg))


    msg = "0010010100011110011111110"
    # key = rand_key(len(msg))
    rand = random2.randint(1, 10000000)
    key = LCG(rand, 1)[0]
    print('key is ', key)
    binkey = bin(key)[2:]
    print('bin key is ', binkey, ' type is ', type(binkey))
    print('length of key is {} and msg is {}'.format(len(binkey), len(msg)))

    lkey = len(binkey)
    lmsg = len(msg)

    quo = lmsg / lkey
    rem = lmsg % lkey

    print('quo is {} and rem is {}'.format(int(quo), rem))

    fkey = ''
    for i in range(int(quo)):
        fkey += binkey
    
    fkey += binkey[:rem]

    print('final keyy is {} and its length is {} '.format(fkey, len(fkey)))

    
    if sys.argv[1] == availableOpt[1]:
        print('msg is ', msg)
        print('key is ', key)
        print('encrypted msg is: ',enc(msg, fkey))
    elif sys.argv[1] == availableOpt[0]:
        msg = input("Enter the received msg: ")
        key = input("Enter the key used: ")
        print('original msg is: ',dec(msg, key))
