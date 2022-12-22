'''
Half Pyramid_4
Input :
10
5

Output :
24
23 22
21 20 19
18 17 16 15
14 13 12 11 10

'''

N = int(input("Enter A Number : "))
K = int(input("Enter Number Of Rows : "))
num = K*K-1
for i in range(1, K+1):
    row_nums = ""
    for j in range(1, i+1):
        row_nums += str(num) + " "
        num -= 1
    print(row_nums)