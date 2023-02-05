# 1 + x^2/2 + x^3/3 + … x^n/n


n = int(input("Enter The Value Of N : "))
x = int(input("Enter The Value Of X : "))

sum = 1
for i in range(2, n+1):
    sum = sum + ((x**i) / i)
print("Value is : ", (round(sum, 2)))