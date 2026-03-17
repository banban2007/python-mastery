#3_abstract.py

from abc import ABC, abstractmethod

class Bird(ABC):
	def eat(self):
		print('Eating')

	@abstractmethod	
	def fly(self):
		pass
		
bird = Bird()
#TypeError: Can't instantiate abst....