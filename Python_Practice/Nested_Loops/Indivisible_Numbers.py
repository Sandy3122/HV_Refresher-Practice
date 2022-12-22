# Indivisible Numbers
#Case_1 :

# N = int(input("Enter A Number : "))
# count = 0
# for i in range(1, N+1):
#     is_divisible = "True"
#     for j in range(2,11):
#         if(i%j == 0):
#             is_divisible = "False"
#             break
#     if(is_divisible == "True"):
#         count += 1
# print(count)



#Case_2 :

N = int(input("Enter A Number : "))
count = 0
for i in range(1, N+1):
    is_divisible = "True"
    if(i%2 != 0 and i%3 != 0 and i%4 != 0 and i%5 != 0 and i%6 != 0 and i%7 != 0 and i%8 != 0 and i%9 != 0 and i%10 != 0):
        count += 1
print(count)



#Case_3 :

# def isDivisible(K):
#     counter=0
#     for n in range(2,11):
#         if K%n==0:
#             counter+=1
#     return (counter>0)


# N=int(input())
# indivisibleNumber=0
# for i in range(1,N+1):
#     if not isDivisible(i):
#         indivisibleNumber +=1
# print(indivisibleNumber)