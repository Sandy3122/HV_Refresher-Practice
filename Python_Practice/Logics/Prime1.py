#Prime Number
num = int(input("Enter A Number : "))
if(num>1):
    for i in range(2,num):
        if(num%i==0):
            print(num," Is Not A Prime number")
            print(i, "Times ",num//i,"is",num)
            break
    else:
        print(num, " Is A Prime Number") 
else:
    print(num,"Is Not A Prime Number") 