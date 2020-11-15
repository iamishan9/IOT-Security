# importing all the libraries
from rapid_exponentiation import exp_w_recursion,exp_wo_recursion
import time
import timeit
from utils import bcolors

# performing exponentiation with recursion
start_time1 = timeit.default_timer()
exp_res1=exp_w_recursion.find_expo(2,500)
time_exec1=timeit.default_timer() - start_time1

# performing exponentiation without recursion
start_time2 = timeit.default_timer()
exp_res2,steps=exp_wo_recursion.find_expo(2,500)
time_exec2=timeit.default_timer() - start_time2

# printing the answers obtained
print("\n")
print(bcolors.OKGREEN+"Performing exponetiation with recursion:\n"+bcolors.ENDC,exp_res1)
print("\n")
print(bcolors.OKGREEN+"Performing exponentiation without recursion:\n"+bcolors.ENDC,exp_res2)
print(bcolors.OKBLUE+"Number of steps for non-recursive exponentiation:{}".format(steps)+bcolors.ENDC)
print("\n")

# comparing the time of execution using the two methods
print(bcolors.OKGREEN+"Algorithm\t\t\tTime of execution"+bcolors.ENDC)
print("exp with recursion:\t{}".format(time_exec1))
print("exp without recursion:\t{}".format(time_exec2))
print("\n")