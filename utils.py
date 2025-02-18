# importing all libraries
import time

# for showing the text in colors
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


# for taking seed as time 
class Seed(object):
    # Function that generates seed
    def generate_seed(self):
        pass

class TimeSeed(Seed):
    """ Generates seed from current time """
    def generate_seed(self):
        return time.time()


