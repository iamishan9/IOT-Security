from rapid_exponentiation import exp_w_recursion,exp_wo_recursion
import time
import timeit

start_time1 = timeit.default_timer()
exp_res1=exp_w_recursion.find_expo(2,500)
time_exec1=timeit.default_timer() - start_time1
print("Time of execution for exponentiation with recursion: {}".format(time_exec1))
start_time2 = timeit.default_timer()
exp_res2,steps=exp_wo_recursion.find_expo(2,500)
time_exec2=timeit.default_timer() - start_time2
print("Time of execution for exponentiation without recursion: {}".format(time_exec2))
print("Performing exponetiation with recursion:\n",exp_res1)
print("Performing exponentiation without recursion:\n",exp_res2)
print("Number of steps for non-recursive exponentiation:{}".format(steps))