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
14 13 12 11 10-\;m

'''

# N = int(input("Enter A Number : "))
# K = int(input("Enter Number Of Rows : "))
# num = N
# for n in range(K):
#     num = n + num
# res = N + num
# for i in range(1, K+1):
#     row_nums = ""
#     for j in range(1, i+1):
#         row_nums += str(num) + " "
#         res -= 1
#     print(row_nums)

n = int(input())
k = int(input())
c = n-1
for i in range(k):
    for j in range(i+1):
        c = c+1 
for i in range(k):
    for j in range(i+1):
        print(c,end=" ")
        c=c-1
    print()