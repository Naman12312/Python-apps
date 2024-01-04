class Employee:
    no_of_leaves = 8
    var = 8
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
# class Programmer(Employee):
#     def __init__(self,name,Salary,favourite_food,lang):
#         self.name = name
#         self.salary = Salary
#         self.favourite_food = favourite_food
#         self.lang = lang
#     def printprog(self):
#         return f"Programmer's Name is : {self.name}, Salary is: {self.salary} and favourite food is: {self.favourite_food}, Programming Language is : {self.lang}"
Shalu = Employee("Shalu",99999999,['???'])
Dhruv_Bhaiya = Employee("Dhruv",99999999,("dal rice", "Chole rice","Rajama rice", "Kari rice"))
Tripti = Employee("Tripti",99999999,("Dal rice", "kari rice"))
class Player:
    no_of_games = 4
    var = 9
    def __init__(self,name,game):
        self.name = name
        self.game = game
    def printdetails(self):
        print(f"Name is : {self.name}, Game is : {self.game}")
class CoolProgammer(Employee, Player):
    lang = "Python"
    def printlang(self):
        print(self.lang)
punya = Player("Punya", ["Free fire", "Among us"])
Chachaji = CoolProgammer("Vinod",99999999,("all"))
Naman = CoolProgammer("Naman",99999999,("dal rice", "Chole rice","Rajama rice", "Kari rice"))
print(Naman.var)



'''
Next: Multilevel inheritance - Python tourtial for absolute beginners in hindi. #63
'''
