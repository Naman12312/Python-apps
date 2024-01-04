class Employee:
    no_of_leaves = 8
    def __init__(self,name,Salary,favourite_food):
        self.name = name
        self.salary = Salary
        self.favourite_food = favourite_food
    def printdetails(self):
        return f"Name is : {self.name}, Salary is: {self.salary} and favourite food is: {self.favourite_food}"
    @classmethod
    def Change_leaves(cls,leaves):
        cls.no_of_leaves = leaves
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def print2(string):
        print(string)
Tripti = Employee("Tripti",99999999,"Kari rice, Dal rice")
Naman = Employee.from_str("Naman-9999999-kari rice,dal rice,cholerice,rajmarice")
Naman.Change_leaves(1)
print(Naman.no_of_leaves)
print(Tripti.no_of_leaves)
print(Naman.printdetails())
print(Tripti.printdetails())
Naman.print2(f"Hello! I am {Naman}" + f" My name is {Naman.name}")
print()