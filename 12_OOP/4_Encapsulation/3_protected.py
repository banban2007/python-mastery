class Employee:
    _id = 10 

    def get_id(self):
        print("Id inside class", self._id)

emp = Employee()

emp.get_id()
print("Id outside class", emp._id)
