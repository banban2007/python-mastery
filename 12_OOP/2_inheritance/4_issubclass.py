class Animal:
    def eat(self):
        print("Eating")

class Brid(Animal):
    def fly(self):
        print("Flying")

print(issubclass(Animal,Brid))
print(issubclass(Brid,Animal))