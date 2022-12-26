#Integer Factorization


def factorisation(n):
    fact = []
    i = 2
    while i<=n:     
        if n%i==0:      
            fact.append(i)
            n//= i
        else:
            i+=1
    return fact

n = int(input("Enter A Number : "))
print(factorisation(n))

