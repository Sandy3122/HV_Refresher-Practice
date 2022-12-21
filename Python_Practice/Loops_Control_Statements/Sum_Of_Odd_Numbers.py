#Sum Of Odd Numbers
N = int(input("Enter A Number : "))
odd_sum = 0
for i in range(1, N+1, 2):
    odd_sum += i
print(odd_sum)