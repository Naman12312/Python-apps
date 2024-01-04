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
hindustani_supporter = Employee("hindustani", "_supporter")
nikhil_raj_pandey = Employee("nikhil", "raj_pandey")
print(hindustani_supporter.email)
hindustani_supporter.email = "This.That@CodeWithHarry.com"
del hindustani_supporter.email
# print(hindustani_supporter.email)