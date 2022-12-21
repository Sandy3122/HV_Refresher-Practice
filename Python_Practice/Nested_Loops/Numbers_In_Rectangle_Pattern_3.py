#Numbers In Rectangle Pattern_3 
M = int(input("Enter Number Of Rows : "))
N = int(input("Enter Number Of Colums : "))
num = 1
for i in range(1, M+1):
    row_num = ""
    for j in range(1, N+1):
        row_num += str(num) + " "
        num += 1
    print(row_num)