# M = int(input("Enter number Of Rows : "))
# N = int(input("Enter number Of Columns : "))
# for i in range(M+2):
#     # print(i)
#     for j in range(N+2):
#         # print(j)
#         if((i==0 and j==0) or (i==0 and j==N+2) or (i==M+2 and j==0) or (i==M+2 and j==N+2)):
#             print("+", end=" ")
#         if(i == 1 or i == M):
#             print("*", end=" ")
#         if(j == 0 or j == N+2):
#             print("|", end=" ")
#         # else:
#         #     print(" ", end=" ")
#     print()


M = int(input("Enter number Of Rows : "))
N = int(input("Enter number Of Columns : "))
for i in range(N+2):
    if i==0 or i==N+1:
        print("+"+"-"*M+"+")
    else:
        print("|"+" "*M+"|")