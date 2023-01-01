# Create a class - Student. Use the method concept, 
# to fetch student name and marks for them

class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks=marks
    def student1(self):
        # print("Hello, My Name Is: ", format(self.name,self.marks))
        print(f"Hello, My Name Is {self.name} and my marks are {self.marks}")
    def student2(self):
        # print(f"Hello, My Name Is {self.name} and my marks are {self.marks}")             #Formated String
        print("Hello, My Name Is %s and my marks are %s" %(self.name, self.marks))          #Formated String
        #you can also use %d, %f, %r for integers, floats, string representations of objects respectively
      
Std1 = Student("Seeram", 99)
Std2 = Student("Sandeep", 98)
Std1.student1()                 #Funtion Calling From Parent Class
Std2.student2()

# print('Hello there {} and {}'.format(name1, name2))