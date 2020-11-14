# -*- coding: utf-8 -*-

def gen_prime(end):
    start=2
    # list of prime numbers
    primes = []
    start = 2 if start < 2 else start
    for i in range(start,end+1):
        primes.append(i)

    i = 2
    #from 2 to (number/2)
    while(i <= int(end/2)):
        #if i is in list
        #then we delete its multiples
        if i in primes:
            #j will give multiples of i,
            #starting from 2*i
            for j in range(i*2, end+1, i):
                if j in primes:
                    #deleting the multiple if found in list
                    primes.remove(j)
        i = i+1
    
    return primes

# printing the remaining list
# print (primes)