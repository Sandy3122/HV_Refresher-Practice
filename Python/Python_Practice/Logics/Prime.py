#Prime Number Check
############
## Case_1 ##
############
# num = int(input("Enter Number To Check Prime Or Not : "))
# flag = False
# if(num>1):
#     for i in range(2, num):
#         if(num%i == 0):
#             flag = True
#             break
# if(flag):
#     print(f"{num} Is Not A Prime Number")
# else:
#     print(f"{num} Is A Prime Number")


############
## Case_1 ##
############
num = int(input("Enter Number To Check Prime Or Not : "))
factors = 0
for i in range(2, num):
    if(num%i == 0):
        factors += 1
if(factors ==0 ):
    print(f"{num} Is A Prime Number")
else:
    print(f"{num} Is Not A Prime Number, Bacause It Has More Than Two Factors({factors+2})")
