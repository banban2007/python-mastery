class Animal:
	def speak(self):
		print("speaking")
		
class Dog(Animal):
	def speak(self, **kwargs):
		if 'word' in kwargs and len(kwargs) == 1:
			word = kwargs['word']
			print("speaking",word)
		if ('word' and 'times' in kwargs) and len(kwargs) == 2:
			word = kwargs['word']
			times = kwargs['times']
			print("speaking",word * times)

		if not kwargs:
			print("speaking")
d = Dog()

d.speak()
d.speak(word='woofwoof')
d.speak(word='woofwoof',times=2)