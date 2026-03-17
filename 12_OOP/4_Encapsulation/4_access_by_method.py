class Employee:
    __id = 10 

    def change_id(self, id):
        if id > 20:
            print("Id is not permitted")
        else:
            self.__id = id
            print("after change ", self.__id)

    def get_id(self):
        print("Id inside class", self.__id)

emp = Employee()
emp.get_id()
emp.change_id(18)
emp.get_id()