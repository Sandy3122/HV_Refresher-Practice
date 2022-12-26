#Greatest Common Divisor

print("Greatest Common Divisor")
M = int(input("Enter A Number : "))
N = int(input("Enter A Number : "))
if M > N:
    smallest_num = N
else:
    smallest_num = M
gcd = smallest_num
for i in range(1,smallest_num+1):
    if(N % i == 0) and (M % i == 0):
        print(gcd)