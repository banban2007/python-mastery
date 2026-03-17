class Animal:
    def eat(self):
        print("Eating")

class Animal2:
    def fly(self):
        print("Eating")

class Brid(Animal):
    def fly(self):
        print("Flying")

eagle = Brid()

print(isinstance(eagle,Brid))
print(isinstance(eagle,Animal))
print(isinstance(eagle,Animal2))