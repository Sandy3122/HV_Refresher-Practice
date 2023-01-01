#Prime Numbers From N To M

N = int(input("Enter A Number : "))
M = int(input("Enter A Number : "))
for i in range(N,M):
    for j in range(2, i):
        # print("Inner", j)
        if( i%j == 0 ):
            break
    else:
        print(i)