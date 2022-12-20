'''
Given two numbers A and B, Find the Kth Digit from right of A^B
'''

# num1 = int(input("Enter A 1st Number : "))
# num2 = int(input("Enter A 2nd Number : "))
# kth = int(input("Enter Kth Digit To Find : "))
# # lst = []
# if(num1 and num2 > 0):
#     pow = num1**num2
# split_pow = str(pow)
# print(split_pow)
# print(split_pow[-1])


num1 = int(input("Enter A 1st Number : "))
num2 = int(input("Enter A 2nd Number : "))
kth = int(input("Enter Kth Digit To Find : "))
if(num1 and num2 > 0):
    pow = num1**num2
my_list = [int(x) for x in str(pow)]
print(my_list[kth])
