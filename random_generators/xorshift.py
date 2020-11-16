# # imports for abstract classes
# from abc import ABCMeta, abstractmethod
# import time

# perform xorshift
def xor_shift(start, end, seed):

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