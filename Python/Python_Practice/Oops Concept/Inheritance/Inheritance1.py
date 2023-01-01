#Inheritance

''' Self (Keyword): self parameter is a referance to the current instance of the class,
and is used to access variables that belongs to the class. '''

class Person(object):         #Creating Persons Class
    def __init__(self,name):  #Default Constructor
        self.name=name
    def getName(self):        #Creating Method
        return self.name
    def isEmployee(self):
        return False

class Employee(Person):       # Creating Another Class which has all properties of Person Class
    def isEmployee(self):
        return True

emp = Person('Sandeep')         #Creating object with Person class
print(emp.getName(),emp.isEmployee())

emp = Employee('Seeram')        #Creating object with Employee class
print(emp.getName(),emp.isEmployee())