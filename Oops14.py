class Employee:
    no_of_leaves = 8
    var = 8
    _emp = 7
    __emem = 3
    def __init__(self,name,Salary,favourite_food):
        self.name = name
        self.salary = Salary
        self.favourite_food = favourite_food
    def printdetails(self):
        return f"Emplyee's Name is : {self.name}, Salary is: {self.salary} and favourite food is: {self.favourite_food}"
    @classmethod
    def Change_leaves(cls,leaves):
        cls.no_of_leaves = leaves
    @classmethod
    def from_str(cls,string):
        return cls(*string.split("-"))
    @staticmethod
    def print2(string:any):
        print(string)
    def __add__(self, other):
        return self.salary + other.salary
    def __truediv__(self,other):
        return self.salary / other.salary
    # Special methods:
    def __mul__(self, other):
        return self.salary * other.salary
    def __sub__(self, other):
        return self.salary - other.salary
    def __floordiv__(self, other):
        return self.salary // other.salary
    def __mod__(self, other):
        return self.salary % other.salary
    # Special method ends...
    def __repr__(self):
        return self.printdetails() + "Hello"
    def __str__(self):
        return self.printdetails()
emp1 = Employee("Naman", 2000, "Rice with shole , rajma, dal, kari")
emp2 = Employee("Harry", 1000, "Rice with shole , rajma, dal, kari")
print(emp1 + emp2)
print(emp1 / emp2)
print(emp1 * emp2)
print(emp1 - emp2)
print(emp1 // emp2)
print(emp1 % emp2)
print(emp1)
"""
Next: Abstract Base Class & @abstractmethod | Python Tutorials For Absolute Beginners In Hindi #68
"""