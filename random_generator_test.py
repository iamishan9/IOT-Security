from random_generators import lcg,glsfr,mersenne_twister as mt, bbs, isaac, xorshift as xs
import time

class Seed(object):
    # Function that generates seed
    def generate_seed(self):
        pass


class TimeSeed(Seed):
    """ Generates seed from current time """

    def generate_seed(self):
        return time.time()

print("Generating 10 random numbers using Linear Congruetional Generator (LCG):")
for i in range(10): 
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
    key = lcg.LCG(random_number, 1)[0]
    print(key)

print("\nGenerating 10 random numbers using XORshift:")
# mt_rn = mt.mersenne_rng(1131464071)
for i in range(10):
    print(xs.xor_shift(1,2**20,TimeSeed()))

print("\nGenerating 10 random numbers using Linear feedback shift registers(LFSR):")
lfsr_rn = glsfr.LfsrRandom(0b10110100000000001, 1)
for i in range(10):
	print(lfsr_rn.random(number_bit=20))

print("\nGenerating 10 random numbers using Mersenne-twister:")
mt_rn = mt.mersenne_rng(1131464071)
for i in range(10):
    print(mt_rn.get_random_number())


print("\nGenerating 10 random numbers using Blum Blum Shub:")
bbs_rn = bbs.BBS(286, 100, 200)
gen = bbs_rn.Generator()
for _ in range(0,10):
    x = next(gen)
    print(x)

print("\nGenerating 10 random numbers using ISAAC:")
issac_rn = isaac.Isaac()
for _ in range(0,10):
    number = issac_rn.rand()
    print(number)

