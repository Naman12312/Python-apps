class Employee:
    def __init__(self,name,Salary,favourite_food):
        self.name = name
        self.salary = Salary
        self.favourite_food = favourite_food
    def printmethods(self):
        return f"Name is : {self.name}, Salary is: {self.salary} and favourite food is: {self.favourite_food}"
Tripti = Employee("Tripti",99999999,"Kari rice, Dal rice")
Naman = Employee("Naman",99999999,"Dal rice,Kari rice,Shole rice,rajma rice")