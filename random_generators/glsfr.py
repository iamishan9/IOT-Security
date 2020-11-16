# -*- coding: utf-8 -*-
"""
GLSFR random generator
constains a class for lsfr random
"""
import random
class LfsrRandom(random.Random):
	
	def __new__(cls, *args, **kwargs):  
		return random.Random.__new__(cls, random.random())
	
	# initializing
	def __init__(self, charis, state):
		assert isinstance(charis, int)
		assert isinstance(state, int)
		
		if charis < 0:
			raise ValueError("Invalid characteristic polynomial - negative")
		if charis.bit_length() < 2:
			raise ValueError("Invalid characteristic polynomial - degree too low")
		if state == 0:
			raise ValueError("Invalid state polynomial - all zero")
		if state.bit_length() >= charis.bit_length():
			raise ValueError("Invalid state polynomial - degree >= char poly degree")
		
		self.characteristic = charis
		self.degree = charis.bit_length() - 1
		self.state = state
	
	# use bit 0 in the LSFR state as result
	# multiply by x
	# If degree of state polynomial matches degree of characteristic polynomial
	# Then subtract the characteristic polynomial from the state polynomial
	def randbit(self):
		result = self.state & 1                   
		self.state = self.state << 1             
		if (self.state >> self.degree) & 1 != 0:  
			self.state ^= self.characteristic      
		return result
	
	
	def getrandbits(self, k):
		result = 0
		for i in range(k):
			result = (result << 1) | self.randbit()
		return result
	
	
	def random(self,number_bit=20):
		return self.getrandbits(number_bit) 


