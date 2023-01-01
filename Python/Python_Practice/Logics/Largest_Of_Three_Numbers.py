#Largest Of Three Numbers

# num1 = int(input("Enter A 1st Number : "))
# num2 = int(input("Enter A 2nd Number : "))
# num3 = int(input("Enter A 3rd Number : "))
# if(num1>=num2 and num1>=num3):
#     largest = num1
# elif(num2>=num1 and num2>=num3):
#     largest = num2
# else:
#     largest = num3
# print(f"Largest Number Among Three Numbers Is : {largest}")

############
## Case 4 ##
############
#In Functions

largest = 0
def largestOfThreeNumbers(num1, num2,num3):
    if(num1>=num2 and num1>=num3):
        largest = num1
    elif(num2>=num1 and num2>=num3):
        largest = num2
    else:
        largest = num3
    return largest
num1 , num2, num3 = input("Enter Three value: ").split()
print(largestOfThreeNumbers(num1, num2, num3))