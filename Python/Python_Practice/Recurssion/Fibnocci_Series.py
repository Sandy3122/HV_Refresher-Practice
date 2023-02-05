# Write a program to find a fibnocci Series Using Recursion


def fibnocci(n):
    if(n <= 1):
        return n
    else:
        return(fibnocci(n-1) + fibnocci(n-2))

n = int(input("Enter A Number : "))
print("Fibnocci Series Are : ")
for i in range(n):
    print(fibnocci(i))
    