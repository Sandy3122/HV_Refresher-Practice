'''
Half Pyramid_3
Input :
10
5

Output :
10
11 12
13 14 15
16 17 18 19
20 21 22 23 24

'''

N = int(input("Enter A Number : "))
K = int(input("Enter Number Of Rows : "))
num = N
for i in range(1, K+1):
    row_nums = ""
    for j in range(1, i+1):
        row_nums += str(num) + " "
        num += 1
    print(row_nums)