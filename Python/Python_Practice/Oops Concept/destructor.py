class Employee: #Creating Class
    def __init__(self): # Initializing
        print("Employee Created")
    def __del__(self): # Deleting (Calling destructor)
        print("Employee Deleted")

#Craeting an object
emp = Employee()
del emp
emp = Employee()