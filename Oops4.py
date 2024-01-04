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
Tripti = Employee("Tripti",99999999,"Kari rice, Dal rice")
Naman = Employee("Naman",99999999,"Dal rice,Kari rice,Shole rice,rajma rice")
Naman.Change_leaves(1)
print(Naman.no_of_leaves)
print(Tripti.no_of_leaves)
print(Naman.printdetails())
print(Tripti.printdetails())
'''Next:'''
'''
58-Class methods as alternative constructors
'''