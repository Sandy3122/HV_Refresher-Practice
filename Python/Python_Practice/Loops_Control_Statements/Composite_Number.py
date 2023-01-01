#Composite Number

# N = int(input("Enter A Number : "))
# factors = 0
# for i in range(2, N):
#     if(N % i == 0):
#         factors += 1
        # print(factors)
# if(factors == 0):
#     print("False")
# else:
#     print("True")


N = int(input("Enter A Number : "))
factors = 0
for i in range(2, N):
    if(N % i == 0):
        factors += 1
        # print(factors)
if(factors >= 1):
    print("True")
else:
    print("False")
