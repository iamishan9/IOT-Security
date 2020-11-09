# with recursion
def fast_exp(X, e):
  if e==0:
    return 1

  if e%2==0:
    return fast_exp(X,e/2)**2
  else:
    return fast_exp(X,e-1)*X

# print(fast_exp(2,5))

def without_recursion(X, e):
  e = bin(e)[3:] 
  e = str(e)
  print('e is {}'.format(e))
  word = ''
  for x in e:
    if x=='0':
      word += 'S'
    else:
      word += 'SX'
  print('word is {}'.format(word))

  res = X
  step = 0
  for x in word:
    step += 1
    if x == 'S':
      res *= res
    else:
      res *= X

  return res, step

result = without_recursion(2, 5)
print('result is {} which was done in {} steps'.format(result[0], result[1]))

#test
# print(pow_h(2,4,100))
# for i in range(16):
#     print(i, 2**i, pow_h(2, i, 100))
