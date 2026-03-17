class Brid:
    name = "Crow"
    size = 10
    color = "black"
    food = "rice"

    def eat(self):
        print(self.name, "is eating",self.food)

b = Brid()
b.eat()
print(b.name)
print(Brid.name)