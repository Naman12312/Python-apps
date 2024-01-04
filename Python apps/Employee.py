class Employee:
    increasment=2
    def __init__(self,fname,lname,salary,work):
        self.fname = fname
        self.lname = lname
        self.work = work
        self.salary = salary
    
    def increase(self):
        self.salary=(self.salary * Employee.increasment**3)
    @classmethod
    def c_increasment(cls,amount):
        cls.increasment=cls.increasment*amount
    @classmethod
    def from_str(cls,emp_sring):
        fname,lname,salary,work=emp_sring.split("-")
        return cls(fname,lname,salary,work)
    @staticmethod
    def officeisopen(day):
        if day=="Thursday":
            return False
        else:
            return True
class Programmer(Employee):
    def __init__(self,fname,lname,salary,work,prolan,exp):
        super().__init__(fname,lname,salary,work)
        self.prolan=prolan
        self.exp=exp
    def increase(self):
        self.salary=(self.salary * Employee.increasment**3)
Naman=Programmer("Naman","sharma",9999999999,"many work","Python","1 year")
Didi=Programmer("Tripti","Sharma",999999999999,"many work","Javascript","1 year")
Dhruv_bhaiya=Employee("Dhruv","Sharma",9999999999999,"many work")
print(Naman.fname,Naman.lname)
print("Programming language:",Naman.prolan)      
print("officeopen=",Employee.officeisopen("Sunday"))
print(f"work:",Naman.work)
print(f"Salary:",Naman.salary)
print(Didi.fname,Didi.lname)
print(f"work:",Didi.work)
print(f"Salary:",Didi.salary)
print(f"Programming language:",Didi.prolan)
# print(Naman.salary)
Employee.c_increasment(2)
Naman.increase()
print(Dhruv_bhaiya.fname,Dhruv_bhaiya.lname)
print("salary:",Dhruv_bhaiya.salary)
print("work:",Dhruv_bhaiya.work)
# print(dir(Employee))
# print(dir(Employee))
# print(dir(Programmer))
# help(Employee)
# help(Programmer)