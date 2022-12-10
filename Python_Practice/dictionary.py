#Dictionary
dic = {1:'Seeram',2:'Sandeep', 3:'Lakshman', 4:'Kumar'}
print(dic[1])
print(dic.values()) # To print all the values
print(dic.keys()) # To print all the keys
dic[5] = 'From'
dic[6] = 'Mechanical Engineering'
print(dic.values()) # To print all the values
print()

dic1 = {
    "College":'Aditya Engineering College',
    "Location":'Surampalem, AP',
    "Roll No.":'20P35A0387',
    "Department":'Mechanical Engineering'
}
for info in dic1: 
    print(info) # It will only shows the keys
print()
for val in dic1: 
    print(dic1[val]) # It will only shows the values

#taking inputs for using for loop
College = {}
for i in range(3):
    name = input("Enter name: ")
    rollnumber = input("Enter Roll Number: ")
    College[name] = rollnumber
print(College)

#Getting input from user and print it in a dictionary formate
# name = input("Enter name: ")
# rollnum = input("Enter Roll Number: ")
# print({name:rollnum})