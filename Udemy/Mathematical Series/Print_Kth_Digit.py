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

#Case_1

# num1 = int(input("Enter A 1st Number : "))
# num2 = int(input("Enter A 2nd Number : "))
# kth = int(input("Enter Kth Digit To Find : "))
# if(num1 and num2 > 0):
#     pow = num1**num2
# my_list = [int(x) for x in str(pow)]
# print(my_list[kth])


#Case_2
def kthDigit(N1, N2, K):
    pow = N1 ** N2
    temp = 0
    while(K > 0):
        temp = pow%10
        pow = pow // 10
        K-=1
    len_pow = len(str(pow))
    # if(K > len_pow):
    #     print(f"{K} Is Out Of Range")
    return temp

N1 = int(input("Enter A 1st Number : "))
N2 = int(input("Enter A 2nd Number : "))
K = int(input("Enter Kth Digit To Find : "))
print(kthDigit(N1, N2, K))