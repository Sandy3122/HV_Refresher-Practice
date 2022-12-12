# x = range(6)        #numbering starts from ( 0 to 5 ) ;  Always range will be ( n-1 )
# for num in x:
#     print(num)

# n = int(input("Enter A Number : "))
# for i in range(1, n+1):
#     print(i, end=" ")

#Addition And Average Of n Numbers
num = int(input("Enter A Numeber: "))
total=0
for i in range(1, num+1):
    total+=i
print(f"Sum of all numbers upto {num} Is : {total}")
print(f"Average of all numbers upto {num} Is : {total/num}")
print("Average of all numbers upto %s Is : %s" %(num, total/num))
