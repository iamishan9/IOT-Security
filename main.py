import time
import os
import sys
import string
import random
class Seed(object):
    # Function that generates seed
    def generate_seed(self):
        pass


class TimeSeed(Seed):
    """ Generates seed from current time """

    def generate_seed(self):
        return time.time()


help = """python otp.py -e|-d
-e for encryption
-d for decryption """


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

def random(start, end, seed):

    random_number = seed.generate_seed()

    # Get number after decimal point of seed because these are the numbers that actually vary
    random_number = random_number % 1
    random_number = str(random_number)

    # Check if the number is decimal first
    if random_number.find('.') != -1:
        random_number = random_number.split('.')[1]

    # Do not split if no decimal point and just take the integer as it is
    random_number = int(random_number)

    random_number ^= (random_number << 21)
    random_number ^= (random_number >> 35)
    random_number ^= (random_number << 4)

    # Convert the generated number to lie between start and end
    random_number = random_number % end
    if random_number < start:
        random_number = random_number + start

    return random_number


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
    seed=TimeSeed()
    random_number = seed.generate_seed()
    # Get number after decimal point of seed because these are the numbers that actually vary
    random_number = random_number % 1
    random_number = str(random_number)

    # Check if the number is decimal first
    if random_number.find('.') != -1:
        random_number = random_number.split('.')[1]

    # Do not split if no decimal point and just take the integer as it is
    random_number = int(random_number)
    start_time = time.time()
    key = LCG(random_number, 1)[0]
    t1=time.time()-start_time
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
        print('original msg is: ',dec(msg, fkey))
