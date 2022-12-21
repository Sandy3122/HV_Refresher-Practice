#Stripped Rectangle
M = int(input("Enter Numbers Of Rows : "))
N = int(input("Enter Numbers Of Columns : "))
for i in range(1, M+1):
    for j in range(1, N+1):
        if(i % 2 == 1):
            print("+" , end=" ")
        else:
            print("-" , end=" ")
    print()