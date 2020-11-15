from random_generators import lcg, glsfr, mersenne_twister as mt, bbs, isaac, xorshift as xs
import time
import timeit
import numpy as np
from utils import bcolors


class Seed(object):
    # Function that generates seed
    def generate_seed(self):
        pass


class TimeSeed(Seed):
    """ Generates seed from current time """

    def generate_seed(self):
        return time.time()


list_lcg_rn = []

lcg_time, xorshift_time = 0, 0
print(bcolors.OKGREEN+"Generating 10 random numbers using Linear Congruetional Generator (LCG):", bcolors.ENDC)
for i in range(10):
    time.sleep(0.01)
    seed = TimeSeed()
    random_number = seed.generate_seed()
    # Get number after decimal point of seed because these are the numbers that actually vary
    random_number = random_number % 1
    random_number = str(random_number)
    # Check if the number is decimal first
    if random_number.find('.') != -1:
        random_number = random_number.split('.')[1]
    # Do not split if no decimal point and just take the integer as it is
    random_number = int(random_number)
    start_time = timeit.default_timer()
    key = lcg.LCG(random_number, 1)[0]
    lcg_time = timeit.default_timer()-start_time
    print(key)
    list_lcg_rn.append(key)

print(bcolors.OKGREEN+"\nGenerating 10 random numbers using XORshift:", bcolors.ENDC)
# mt_rn = mt.mersenne_rng(1131464071)
xor_list = []
for i in range(10):
    start_time = timeit.default_timer()
    xs_rn = xs.xor_shift(1, 2**20, TimeSeed())
    xorshift_time = timeit.default_timer()-start_time
    xor_list.append(xs_rn)
    print(xs_rn)

print(bcolors.OKGREEN+"\nGenerating 10 random numbers using Linear feedback shift registers(LFSR):", bcolors.ENDC)
lfsr_rn = glsfr.LfsrRandom(0b10110100000000001, 1)
lsfr_list = []
for i in range(10):
    lsfr_random = lfsr_rn.random(number_bit=20)
    lsfr_list.append(lsfr_random)
    print(lsfr_random)
    
print(bcolors.OKGREEN+"\nGenerating 10 random numbers using Mersenne-twister:",bcolors.ENDC)
mt_rn = mt.mersenne_rng(1131464071)
mt_list = []
for i in range(10):
    mt_rand = mt_rn.get_random_number()
    mt_list.append(mt_rand)
    print(mt_rand)


print(bcolors.OKGREEN+"\nGenerating 10 random numbers using Blum Blum Shub:",bcolors.ENDC)

bbs_list = []
for _ in range(0,10):
    time.sleep(0.01)
    seed=TimeSeed()
    random_number = seed.generate_seed()
    # Get number after decimal point of seed because these are the numbers that actually vary
    random_number = random_number % 1
    random_number=str(random_number)
    # Check if the number is decimal first
    if random_number.find('.') != -1:
        random_number = random_number.split('.')[1]
    # Do not split if no decimal point and just take the integer as it is
    random_number = int(random_number)
    bbs_rn = bbs.BBS(random_number)
    gen = bbs_rn.Generator()
    x = next(gen)
    bbs_list.append(x)
    print(x)


print(bcolors.OKGREEN+"\nGenerating 10 random numbers using ISAAC:",bcolors.ENDC)
issac_rn = isaac.Isaac()
isaac_list = []
for _ in range(0,10):
    number = issac_rn.rand()
    isaac_list.append(number)
    print(number)

print(bcolors.OKGREEN+"\nChecking if the parameters we used for LCG are good and satisfy all requirements\n",bcolors.ENDC)
print("With values a=1140671485, c=128201163, m=2**24 ")
if(lcg.parameters_check_lcg(1140671485,128201163,2**24 )):
    print("The parameters are good.\n")
else:
    print("The parameters are not good.\n")

print("With values a=567, c=992, m=2**15 ")
if(lcg.parameters_check_lcg(567,992,2**15)):
    print("The parameters are good.\n")
else:
    print("The parameters are not good.\n")

print("After checking with different values, we chose the first one.\n")
    

# Randomness of LCG 
print(bcolors.OKBLUE,"Checking the randomness of numbers generated by all algorithms:")
# print(lcg.runs_test(list_lcg_rn,np.median(list_lcg_rn)))
print(bcolors.OKGREEN,'Algorithm             EVEN             ODD             <MEDIAN             >=MEDIAN',bcolors.ENDC)


lcg_test = lcg.random_test(list_lcg_rn, np.median(list_lcg_rn))
print(' LCG                   {}             {}             {}                {}'.format(lcg_test[0], lcg_test[1], lcg_test[2], lcg_test[3]))
# print('\n')

# Randomness of ISAAC
# print(bcolors.OKBLUE,"Checking the randomness of numbers generated by ISAAC:")
# print(lcg.runs_test(list_lcg_rn,np.median(list_lcg_rn)))
isaac_test = lcg.random_test(isaac_list, np.median(isaac_list))
# print(bcolors.OKGREEN,'EVEN             ODD',bcolors.ENDC)
print(' ISAAC                 {}             {}             {}                {}'.format(isaac_test[0], isaac_test[1], isaac_test[2], isaac_test[3]))
# print('\n')

# Randomness of XOR-Shift
# print(bcolors.OKBLUE,"Checking the randomness of numbers generated by XOR-Shift:")
# print(lcg.runs_test(list_lcg_rn,np.median(list_lcg_rn)))
xor_test = lcg.random_test(xor_list, np.median(xor_list))
# print(bcolors.OKGREEN,'EVEN             ODD',bcolors.ENDC)
print(' XOR-Shift             {}             {}             {}                {}'.format(xor_test[0], xor_test[1], xor_test[2], xor_test[3]))
# print('\n')

# Randomness of LSFR
# print(bcolors.OKBLUE,"Checking the randomness of numbers generated by LSFR:")
# print(lcg.runs_test(list_lcg_rn,np.median(list_lcg_rn)))
lsfr_test = lcg.random_test(lsfr_list, np.median(lsfr_list))
# print(bcolors.OKGREEN,'EVEN             ODD',bcolors.ENDC)
print(' LSFR                  {}             {}             {}                {}'.format(lsfr_test[0], lsfr_test[1], lsfr_test[2], lsfr_test[3]))
# print('\n')

# Randomness of Mersenne-Twister
# print(bcolors.OKBLUE,"Checking the randomness of numbers generated by Mersenne-Twister:")
# print(lcg.runs_test(list_lcg_rn,np.median(list_lcg_rn)))
mt_test = lcg.random_test(mt_list, np.median(mt_list))
# print(bcolors.OKGREEN,'EVEN             ODD',bcolors.ENDC)
print(' Mersenne              {}             {}             {}                {}'.format(mt_test[0], mt_test[1], mt_test[2], mt_test[3]))
# print('\n')

# Randomness of Blum blum shub
# print(bcolors.OKBLUE,"Checking the randomness of numbers generated by Blum Blum Shub:")
# print(lcg.runs_test(list_lcg_rn,np.median(list_lcg_rn)))
bbs_test = lcg.random_test(bbs_list, np.median(bbs_list))
# print(bcolors.OKGREEN,'EVEN             ODD',bcolors.ENDC)
print(' BBS                   {}             {}             {}                {}'.format(bbs_test[0], bbs_test[1], bbs_test[2], bbs_test[3]))
print('\n')


print(bcolors.OKGREEN+"\nComparing the time required for random generation using LCG and XORshift\n",bcolors.ENDC)
print("Algorithm\tExecution time")
print("LCG      \t{}".format(lcg_time))
print("XORshift \t{}".format(xorshift_time))


if(lcg_time<xorshift_time):
    print("\nHence, it is proved that LCG is faster.\n")
    


