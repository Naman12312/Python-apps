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

hassh = Employee("Naman", 99999999, "???")
print(hassh._emp)
print(hassh._Employee__emem)
'''
Next : Polymorphism In Python | Python Tutorials For Absolute Beginners In Hindi #64
'''