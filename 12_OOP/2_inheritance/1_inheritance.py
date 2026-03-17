class Animal:
    def eat(self):
        print("Eating")

class Brid(Animal):
    def fly(self):
        print("Flying")
brid = Brid()
brid.eat()
brid.fly()