def fast_exp(X, e):
  if e==0:
    return 1

  if e%2==0:
    return fast_exp(X,e/2)**2
  else:
    return fast_exp(X,e-1)*X

print(fast_exp(2,5))
