#Fibonaacci Series Number

num = int(input("Enter The Number : "))
a, b = 0, 1
count = 0
if(num < 0):
    print("Please Enter A Posituve Number : ")
elif(num == 0):
    print(f"Fibinoseries Upto {num} Is : {a}")
elif(num == 1):
    print(f"Fibinoseries Upto {num} Is : {b}")
else:
    while(count<num):
        print(a)
        nth = a + b
        a = b
        b = nth
        count+=1

############
## Case 2 ##
############
#Optimized Version

# num = int(input("Enter The Number : "))
# a, b = 0, 1
# count = 0
# for i in range(2, num+1):
#     while count < num:
#         print(a)
#         c = a + b
#         a , b = b, c
#         count += 1



############
## Case 3 ##
############

# def fibonacci(n):
#     a = 0
#     b = 1
#     if n < 0:
#         print("Incorrect input")
#     elif n == 0:
#         return a
#     elif n == 1:
#         return b
#     else:
#         print(a)
#         print(b)
#         for i in range(2,n):
#             c = a + b
#             a = b
#             b = c
#             print(c, end=" ")
 
# # Driver Program
# (fibonacci(10))