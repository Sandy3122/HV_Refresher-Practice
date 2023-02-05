# Factorial Of Number Using Recursion


def fact(n):
    if(n <= 1):
        return 1
    else:
        return(n + fact(n-1))

n = int(input("Enter A Number :"))
print("Factorial Of A Number : ", fact(n))