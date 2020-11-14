from symmetric_encryption import otp
import time
from random_generators import lcg

class Seed(object):
    # Function that generates seed
    def generate_seed(self):
        pass


class TimeSeed(Seed):
    """ Generates seed from current time """

    def generate_seed(self):
        return time.time()

def convertBin(msg):
    arr = []
    for i in range (0,len(msg)):
        arr.append(int(msg[i]))
    
    return arr
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


msg = '10001001001001'
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
key = lcg.LCG(random_number, 1)[0]
t1=time.time()-start_time
binkey = bin(key)[2:]

lkey = len(binkey)
lmsg = len(msg)

quo = lmsg / lkey
rem = lmsg % lkey

fkey = ''
for i in range(int(quo)):
    fkey += binkey

fkey += binkey[:rem]

otp_key = otp.rand_key(len(msg))

print("Encrypting message (without using random generator):\n")
encrypted_message=otp.enc(msg,otp_key)
decMsg = otp.dec(encrypted_message, otp_key)
print('Sent message is:\t',msg)
print('Encrypted message is:\t',encrypted_message)
print('Received message is:\t',decMsg)
print("\n")

print("\n\nEncrypting message (using key as RSA generated number):\n")
encrypted_message=enc(msg,fkey)
print('Sent message is:\t',msg)
print('Encrypted message is:\t',encrypted_message)
print('Received message is:\t',dec(encrypted_message, fkey))
print("\n")


if decMsg == msg:
    pyb.LED(2).on()
