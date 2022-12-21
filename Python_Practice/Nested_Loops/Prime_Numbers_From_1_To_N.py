#Prime Numbers From 1 To N
N = int(input())
for i in range(2,N):
    for j in range(2, i):
        # print("Inner", j)
        if( i%j == 0 ):
            break
    else:
        print(i)
  




# #function to check if a given number is prime
# def isPrime(n):
#   #since 0 and 1 is not prime return false.
#   if(n==1 or n==0):
#     return False
    
#   #Run a loop from 2 to square root of n.
#   for i in range(2,int(n**(1/2))+1):
#     #if the number is divisible by i, then n is not a prime number.
#     if(n%i==0):
#       return False

#   #otherwise, n is prime number.
#   return True

# # Driver code
# N = int(input())
# #check for every number from 1 to N
# for i in range(1,N+1):
#   #check if current number is prime
#   if(isPrime(i)):
#     print(i,end=" ")

