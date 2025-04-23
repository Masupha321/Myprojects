class Employee:
    def __init__(self, name, age, salary):
        self.name = name # public variable
        self.__age = age # private variable
        self._salary = salary # protected variable
    def displayEmployee(self):
        print ("Name: ", self.name, "age: ", self.__age, "salary: ", self._salary)

e1=Employee("Masupha", 24, 15000)

print (e1.name)
print (e1._salary)
print(e1.__age)