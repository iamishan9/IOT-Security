'''
Contains a function to generate exponentiation using recursion
'''

def find_expo(X, e):
  if e==0:
    return 1

  if e%2==0:
    return find_expo(X,e/2)**2
  else:
    return find_expo(X,e-1)*X