st = int(input("Hey Enter The Starting Number : "))
ln = int(input("Enter The Ending Number : "))
evenSum = 0
oddSum = 0
for i in range(st,ln+1):
    if(i%2==0):             #For Even Number
        evenSum += i
    else:                   #For Odd Number
        oddSum += i
print("Sum Of Even Numbers In Given Range :  %s" %(evenSum))
print("Sum Of Even Numbers In Given Range : %s" %(oddSum))