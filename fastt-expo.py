def fast_exp(X, e):
  if e==0:
    return 1

  if e%2==0:
    return fast_exp(X,e/2)**2
  else:
    return fast_exp(X,e-1)*X

print(fast_exp(2,5))



def pow_h(base, degree, module):
    degree = bin(degree)[2:]
    r = 1
    for i in range(len(degree) - 1, -1, -1):
        r = (r * base ** int(degree[i])) % module
        base = (base ** 2) % module
    return r

#test
print(pow_h(3,4,100))
# for i in range(16):
#     print(i, 2**i, pow_h(2, i, 100))
