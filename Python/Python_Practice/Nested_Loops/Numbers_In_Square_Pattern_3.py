'''
Numbers In Square Pattern_3

Input :
3

Output :
1 2 3
4 5 6
7 8 9

'''

# N = int(input("Enter A Number : "))
# row_num = ""
# for i in range(1, 4):
#     row_num = row_num + str(i) + " "
# print(row_num)

# row_num = ""
# for j in range(4, 7):
#     row_num = row_num + str(j) + " "
# print(row_num)

# row_num = ""
# for k in range(7, 10):
#     row_num = row_num + str(k) + " "
# print(row_num)


#For Best Case
N = int(input("Enter A Number : "))
num = 1
for i in range(1, N+1):
    row_num = ""
    for j in range(1,N+1):
        row_num = row_num + str(num) + " "
        num += 1
    print(row_num)


# n = int(input())
# number = 1
# for i in range(n):
#   pattern = ""
#   for j in range(n):
#     pattern = pattern + (str(number) + " ")
#     # print(number)
#     # print(pattern)
#     number = number + 1
#   print(pattern)