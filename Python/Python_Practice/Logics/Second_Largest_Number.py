#Second Largest Number:

lst =[]
user_inputs = int(input("Enter Number Of Entries : "))
for i in range(1,user_inputs+1):
    entries = int(input(f"Enter A {i} Number : "))
    lst.append(entries)
lst.sort()
print(lst)
print("the Second Largest Number IS : ", lst[-2])
