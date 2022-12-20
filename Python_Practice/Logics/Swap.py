#Swapping Of Numbers
#Case_1

num1 = int(input("Enter A Number 1 : "))
num2 = int(input("Enter A Number 2 : "))
num1,num2=num2,num1
print(num1)
print(num2)

#Case_2
num1 =int(input("Enter A Number 1 : "))
num2 = int(input("Enter A Number 2 : "))
temp =num1
num1= num2
num2=temp
print(num1)
print(num2)