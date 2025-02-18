# importing all libraies
from symmetric_encryption import otp
import time
from random_generators import lcg
from utils import bcolors, TimeSeed


# message to be encrypted
msg = '10001001001001'

# using time as seed
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
# using seed as milisecond part of time

# generating LCG key
key = lcg.LCG(random_number, 1)[0]

# using proper size
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

# Encyption without using LCG
print(bcolors.OKGREEN+"Encrypting message (without using random generator):\n"+bcolors.ENDC)
encrypted_message=otp.enc(msg,otp_key)
decMsg = otp.dec(encrypted_message, otp_key)
print('Sent message is:\t',msg)
print('Encrypted message is:\t',encrypted_message)
print('Received message is:\t',decMsg)
print("\n")

# Encryption using LCG
print(bcolors.OKGREEN+"\n\nEncrypting message (using key as RSA generated number):\n"+bcolors.ENDC)
encrypted_message=lcg.enc(msg,fkey)
print('Sent message is:\t',msg)
print('Encrypted message is:\t',encrypted_message)
print('Received message is:\t',lcg.dec(encrypted_message, fkey))
print("\n")


# if decMsg == msg:
    # pyb.LED(2).on()
