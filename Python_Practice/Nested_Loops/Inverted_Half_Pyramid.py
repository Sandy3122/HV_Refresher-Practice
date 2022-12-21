'''
Inverted Half Pyramid

Input :
3

Output :
1 2 3
1 2
1

'''

#For Input 4
#Brutt Force Case

# N = int(input("Enter A Number : "))
# row_num = ""
# for i in range(1, 5):
#     row_num = row_num + str(i) + " "
# print (row_num)
# row_num = ""
# for i in range(1, 4):
#     row_num = row_num + str(i) + " "
# print (row_num)
# row_num = ""
# for i in range(1, 3):
#     row_num = row_num + str(i) + " "
# print (row_num)
# row_num = ""
# for i in range(1, 2):
#     row_num = row_num + str(i) + " "
# print (row_num)



#For Best Case
N = int(input("Enter A number : "))
for i in range(1, N+1):
    row_num = ""
    for j in range(1, N+1):
        row_num = row_num + str(j) + " "
    if(N>0):
        N-= 1
    print(row_num)