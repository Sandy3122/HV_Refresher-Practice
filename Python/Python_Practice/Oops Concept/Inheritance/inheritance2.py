class Person(object):                   #Creating The Parent Class Object
    def __init__(self,name,id):         #Parameterised Constructor (Parameters = self, name , id)
        self.name =name
        self.id =id
        # print(self.name ,self.id)
    def display(self):                  #display() is method of the parent class
        print(self.name ,self.id)


emp = Person("Seeram Sandeep",387)
emp.display()

class Emp(Person):                      #Inherited Class Or Child Class Means it having all the properties of Person Class
    def Print(self):                    #display() is method of the child class
        print("Emp Class Is Calling")

empDetails = Emp("Seeram Sandeep",1999)
empDetails.display()                    #Function Calling From Parent Class
empDetails.print()                      #Function Calling From Child Class
