# Create a class - Employee for two employees with some objects. 
# Fetch name,age and salary and display it in the screen.

class Employee:
    company = "Sona Industries"
    def __init__(self,name, age, salary):   #parametrised Constructor or default Constructor
        self.name = name
        self.age = age
        self.salary = salary
        print(self.name,self.age,self.salary)

emp1 =Employee("Sandeep",21,10000)
emp2 =Employee("Seeram",20,100000)

# "Accessing Gloabal variable Inside The Class" #
print(f"{emp1.name} and {emp2.name} are works in {emp1.__class__.company}")
print(f"{emp1.name} and {emp2.name} are works in {emp2.__class__.company}")
print(f"{emp1.name} and {emp2.name} are works in {Employee.company}")



# class Employee(object):
#     def __init__(self,name, age, salary):
#         self.name = name
#         self.age = age
#         self.salary = salary
#     def Emp1(self):                                          
#         print(self.name, self.age, self.salary)

#     def Emp2(self):                                        
#         print(self.name, self.age, self.salary)

# emp1 =Employee("Sandeep",21,10000)
# emp2 =Employee("Seeram",20,100000)
# emp1.Emp1()
# emp2.Emp2()

