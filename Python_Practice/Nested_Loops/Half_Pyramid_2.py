'''
Halif Pyramid_2

Input :
5

Output :
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15

'''

N = int(input("Enter A Number : "))
num = 1
for i in range(1, N+1):
    row_num = ""
    for j in range(1, i+1):
        row_num += str(num) + " "
        num += 1
    print (row_num)
