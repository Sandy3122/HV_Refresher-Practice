# if __name__ == '__main__':
#     n = int(input("Enter A Number To Print N Consecutive Numbers : "))
#     if(n <= 0):print("Please Enter A Positive Number")
#     else:
#         for i in range(1,n+1): 
#             print(i, end="")
#             # print(i, end=" ")
#             # print(i, end="/")

n= int(input("Enter A Number : "))
for i in range(1,n+1,3):
    print(i)
    for j in range(1,n+1,3):
        print(j)