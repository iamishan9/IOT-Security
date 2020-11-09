from prime_gen_test import eratosthenes

prime_numbers = eratosthenes.gen_prime(550)
p, q = 0, 0
p_done = False
# q_done = False

for i in reversed(prime_numbers):
    if not(p_done):
        if i%4==3:
            p=i
            p_done= True
    else:
        if i%4==3:
            q=i
            break

print('p is {} and q is {}'.format(p, q))