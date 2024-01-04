class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname
        # self.email = f"{self.fname}.{self.lname}@CodeWithHarry.com"
    def explain(self):
        return f"This Employee is {self.fname} {self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email was deleted..."
        else:
            return f"{self.fname}.{self.lname}@CodeWithHarry.com"
    @email.setter
    def email(self, string):
        print("Setting now...")
        names = string.split("@")[0]
        self.fname = names.split(".")[0]
        self.lname = names.split(".")[1]
    @email.deleter
    def email(self):
        self.fname = None
        self.lname = None
skillf = Employee("Skill", "F")
# print(dir(skillf))
# print()
# print()
# print()
# print(type(skillf))
# print()
# print()
# print()
# print(id(skillf))
import inspect
# print(inspect.getmembers(skillf))