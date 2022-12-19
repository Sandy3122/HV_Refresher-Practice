#Factorial
#Example : 5! = 5*4*3*2*1 = 120

num = int(input("Enter Number To Check Factorial : "))
res = []
fact = 1                    #Global Variable
if(num < 0): print("Please Return Only Positive Numbers")
elif(num==0): print("The Factorial Of 0 Is : 1")
else:
    for i in range(1 , num+1):
        fact = fact * i
        res.append(fact)
    fact_str = str(fact)
    # print(f"The Factorials Of {num}, Is : {res}")
    print(f"The Factorial Of {num}, Is : {fact}")
