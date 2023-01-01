# Take five inputs from the user. Make sure those inputs are positive numbers 
# (write the code for the same) and then add those numbers. Once the total is displayed in the console.
# Optional - Try to save that number in the file as well (Using the file handling concept.)

''' *** Case1 *** '''
data = open("task1userdata.txt", "a")                               # task2Data.txt has been created and appending th values in it
num1 = int(input("Enter 1st Number: "))                             # Taking inputs from the user
num2 = int(input("Enter 2nd Number: "))
num3 = int(input("Enter 3rd Number: "))
num4 = int(input("Enter 4th Number: "))
num5 = int(input("Enter 5th Number: "))
allInputs = [num1, num2, num3, num4, num5]                          # Arranging all the individual values in the list
print("User Inputs: ", allInputs)
total = (num1 + num2 + num3 + num4 + num5)                          # Total Adding all the inputs

if((num1<=0) or (num2<=0) or (num3<=0) or (num4<=0) or (num5<=0)):  # Checking weather the input is Positive or Negative
    print("Note: Please Enter Only Positive Numbers")
else:
    print("Sum Of All Numbers Is : ",total)                         # Printing the sum of all the values
    print("User Inputs: ", allInputs, file=data)                    # Saving all the input values in the list
    print("Sum Of All Positive Numbers: ",total,"\n", file=data)    # Saving the total value in the file


''' *** Case2 *** '''
'''userInputs = []
total = 0                                   # Creating an empty list
num = int(input("Enter Number Of Elements To Be Added: " ""))
for i in range(num):                        # Iterating till the range
    n = int(input("Enter A Number: "))      # Number of elements as input
    if(n<=0):
        print("Note: Please Enter Only Positive Numbers")
        # break                             # If Condition is flase it will break the loop
    else:
        userInputs.append(n)                # Adding all the positive numbers in list
        total+=n                            # Adding All Positive Numbers
print("User Inputs: ", userInputs)
print("User Inputs: ", userInputs, file=data)
print("Sum Of All Positive Numbers: ",total)          
print("Sum Of All Positive Numbers: ",total,"\n", file=data)'''


''' *** Case2 *** '''
n = int(input("Number of inputs : "))
ls = []
for i in range(n):
    while True:
        m = int(input("Enter a number :"))
        if m >= 0:
            ls.append(m)
            break
        else:
            print("Postive numbers only!")
summ = sum(ls)
data = open("task1userdata.txt", "a") 
print("Given inputs are : ", ls, file=data)
print("Sum of the inputs = ", summ, file = data)