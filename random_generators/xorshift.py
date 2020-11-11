# # imports for abstract classes
# from abc import ABCMeta, abstractmethod
# import time

# ''' ==============================================================================================
# Seed Classes
# ==============================================================================================='''


# class Seed(object):
#     """Abstract class for seeds"""

#     __metaclass__ = ABCMeta

#     @abstractmethod
#     # Function that generates seed
#     def generate_seed(self):
#         pass


# class TimeSeed(Seed):
#     """ Generates seed from current time """

#     def generate_seed(self):
#         return time.time()


# ''' ==============================================================================================
# End Seed Classes
# ==============================================================================================='''


# ''' ==================================================================================================
# Randomizer Classes
# ==================================================================================================='''


# class Randomizer(object):
#     """Abstract class to generate random numbers"""

#     __metaclass__ = ABCMeta

#     @abstractmethod
#     # Function that generates random numbers
#     # 'Decorate' seed onto the random number generator
#     def random(self, start, end, seed):
#         pass


# class XORShiftRandomizer(Randomizer):
#     """XOR Shift Randomizer"""

#     def random(self, start, end, seed):

#         random_number = seed.generate_seed()

#         # Get number after decimal point of seed because these are the numbers that actually vary
#         random_number = random_number % 1
#         random_number = str(random_number)

#         # Check if the number is decimal first
#         if random_number.find('.') != -1:
#             random_number = random_number.split('.')[1]

#         # Do not split if no decimal point and just take the integer as it is
#         random_number = int(random_number)

#         random_number ^= (random_number << 12)
#         random_number ^= (random_number >> 25)
#         random_number ^= (random_number << 27)

#         # Convert the generated number to lie between start and end
#         random_number = random_number % end
#         if random_number < start:
#             random_number = random_number + start

#         return random_number


# ''' ==================================================================================================
# End Randomizer Classes
# ==================================================================================================='''


# if __name__ == "__main__":
#     number_of_numbers = int(input())
#     number_of_digits = int(input())

#     xor_random = XORShiftRandomizer()

#     if number_of_numbers == 0:
#         exit(0)

#     # Calculate start and end of the range from number of digits
#     # start and end are starting as string because 0/9 will be appended to them and start and end will be generated. They will later be converted to integer
#     start = "1"
#     end = "9"
#     if number_of_digits == 0:
#         exit(0)
#     elif number_of_digits == 1:
#         start = 0
#     else:
#         while number_of_digits > 1:
#             start = start + "0"
#             end = end + "9"
#             number_of_digits = number_of_digits - 1

#     start = int(start)
#     end = int(end)

#     while number_of_numbers > 0:
#         print('start is {} and end is {}'.format(start, end))
#         print (xor_random.random(start, end, TimeSeed()))
#         number_of_numbers = number_of_numbers - 1


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