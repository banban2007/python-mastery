class Animal:
    def eat(self):
        print("Eating")

class Brid:
    def fly(self):
        print("Flying")

class BabyBrid(Animal,Brid):
    def walk(self):
        print("walking")

bb = BabyBrid()
bb.eat()
bb.fly()
bb.walk()