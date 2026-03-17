class Animal:
	def speak(self):
		print("speaking")

class Dog(Animal):
	def speak(self):
		print("Barking")

	def speak(self,word):
		print("speaking",word)

	def speak(self,word,times):
		print("speaking",word * times)

d = Dog()

# d.speak()
d.speak('woofwoof')
d.speak('woofwoof',2)