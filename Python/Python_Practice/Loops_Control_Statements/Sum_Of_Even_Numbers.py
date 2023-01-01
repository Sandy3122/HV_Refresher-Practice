#Sum Of Even Numbers
N = int(input("Enter A Number : "))
even_sum = 0
for i in range(2, N+1, 2):
    even_sum += i
print(even_sum)