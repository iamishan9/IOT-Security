# asking for a number 
print ("Enter the a number")
number = int(input())

# list of prime numbers
primes = []
for i in range(2,number+1):
    primes.append(i)

i = 2
#from 2 to (number/2)
while(i <= int(number/2)):
    #if i is in list
    #then we delete its multiples
    if i in primes:
        #j will give multiples of i,
        #starting from 2*i
        for j in range(i*2, number+1, i):
            if j in primes:
                #deleting the multiple if found in list
                primes.remove(j)
    i = i+1

# printing the remaining list
print (primes)