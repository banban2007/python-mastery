class Animal:
    def eat(self):
        print("Eating")

class Brid(Animal):
    def fly(self):
        print("Flying")

class BabyBrid(Brid):
    def walk(self):
        print("walking")

bb = BabyBrid()
bb.eat()
bb.fly()
bb.walk()