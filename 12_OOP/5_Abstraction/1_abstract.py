#1_abstract.py
from abc import ABC, abstractmethod
#ABC = Abstract Base Class
class Bird(ABC):
	def eat(self):
		print('Eating')

	@abstractmethod	
	def fly(self):
		pass

class Eagle(Bird):
	def eat(self):
		print('Eagle Eating')

	def fly(self):
		print('Eagle Flying')

eagle = Eagle()
eagle.eat()
eagle.fly()