class Brid:
    def fly(self):
        return 100

class Eagle:
    def fly(self):
        return 1000

class Crow (Brid):
    def fly(self):
        return 500

brid = Brid()
eagle = Eagle()
crow = Crow()

print(eagle.fly())
print(crow.fly())

print("Brid flying %d Meter Height"%(brid.fly()))
print("Eagle flying %d Meter Height"%(eagle.fly()))
print("Crow flying %d Meter Height"%(crow.fly()))