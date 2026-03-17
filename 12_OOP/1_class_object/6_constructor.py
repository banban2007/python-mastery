class Brid:
    def __init__(self, name, size, color, food):
        self.name = name
        self.size = size
        self.color = color
        self.food = food
    
    def eat(self):
        print(self.name, "is eating", self.food, "size is",self.size)

crow = Brid("Crow", 10, "black", "rice")
crow.eat()

eagle = Brid("Eagle", 100,"gray","mouse")
eagle.eat()