from random import randint

def witness(a,n):
    m = n-1
    y = 1
    while m!=0:
        if m%2==1:
            y=(a*y)%n
            m=m-1
        else:
            b=a
            a= (a*a)%n
            if(a==1 and b!=1 and b!=n-1):
                return True
            m=m/2
    if y!=1:
        return True
    else:
        return False

def millerRabin(n, k=5):
    for i in range(0,k):
        a=randint(1,n-1)
        if(witness(a,n)):
            return True
    return False

print(millerRabin(2097))