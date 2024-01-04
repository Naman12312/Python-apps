import pyttsx3
from pyttsx3.drivers import sapi5
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',195)
class Employee:
    no_of_leaves = 8
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
    @staticmethod
    def speak(audio:str):
        engine.setProperty('voice',voices[0].id)
        engine.say(audio)
        engine.runAndWait()
    @staticmethod
    def femalespeak(audio:str):
        engine.setProperty('voice',voices[1].id)
        engine.say(audio)
        engine.runAndWait()

class Programmer(Employee):
    def __init__(self,name,Salary,favourite_food,lang):
        self.name = name
        self.salary = Salary
        self.favourite_food = favourite_food
        self.lang = lang
    def printprog(self):
        return f"Programmer's Name is : {self.name}, Salary is: {self.salary} and favourite food is: {self.favourite_food}, Programming Language is : {self.lang}"
Shalu = Employee("Shalu",99999999,"???")
Dhruv_Bhaiya = Programmer("Dhruv",99999999,"kari rice,dal rice,cholerice,rajmarice",[])
Tripti = Programmer("Tripti",99999999,"Dal rice, kari rice",['HTML','Javascript'])
Chachaji = Programmer("Vinod",99999999,"all",['C#'])
Naman = Programmer("Naman",99999999,"kari rice,dal rice,cholerice,rajmarice",['Python'])
if __name__=="__main__":
    print(Chachaji.printprog())
    print(Naman.printprog())
    print(Tripti.printprog())
    print(Dhruv_Bhaiya.printprog())
    Shalu.print2(Shalu.printdetails())
    Chachaji.speak(Chachaji.printprog())
    Naman.speak(Naman.printprog())
    Tripti.femalespeak(Tripti.printprog())
    Dhruv_Bhaiya.speak(Dhruv_Bhaiya.printprog())
    Shalu.speak(Shalu.printdetails())
'''
Next: Multiple inheritance - Python tourtial for absolute beginners in hindi. #62
'''

'''
power level of :



@classmethod: (cls), is like the normal bound method but instead of taking the object as first args, takes the class. can be called on class or from an object.
@boundmethod: (self), is the normal bound method which takes the object as first args. can only be called from an object.
@staticmethod: (), is another method with doesnt take anything by default(not even the object itself and the class). can be called from a class or from an object.




THE SAME PROCESS GOES ON FOR JAVA!

'''