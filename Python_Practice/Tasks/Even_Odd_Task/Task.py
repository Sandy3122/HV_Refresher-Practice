# Take an input from the use"r and find out whether the number is even or odd
data =open("S:/HeroVired Refresher/Python/HV_Refresher-Practice/usersData.txt","a")
# data =open("usersData.txt", "a")
num = int(input("Enter The Number To Even Or Odd:" ""))
print("INPUT: ","Enter The Number To Even Or Odd:" " ",num, file=data)

if(num%2 == 0):
    print(num,"The Given Number Is Even Number")
    print("OUTPUT : ",num,"The Given Number Is Even Number","\n", file=data)
else:
    print(num,"The Given Number Is Odd Number")
    print("OUTPUT : ",num,"The Given Number Is Odd Number","\n", file=data)

# files  =open("usersData.txt", "r")
# print(files.readline())
# files.close()