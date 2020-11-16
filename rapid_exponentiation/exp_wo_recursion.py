'''
Contains a function to generate exponentiation without recursion.
'''
def find_expo(X, e):
  e = bin(e)[3:] 
  e = str(e)
#   print('e is {}'.format(e))
  word = ''
  for x in e:
    if x=='0':
      word += 'S'
    else:
      word += 'SX'
#   print('word is {}'.format(word))

  res = X
  step = 0
  for x in word:
    step += 1
    if x == 'S':
      res *= res
    else:
      res *= X

  return res, step