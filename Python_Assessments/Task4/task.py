'''
Question 2 - 

Write a Python program on Series where the user will take some inputs, approx. 5 inputs and then it will display the power of all those inputs, taken in the first series. 


Sample Input - s1 -     1  4   5  6  9

Sample Output - s2 -  1  16  25  36  81
'''

import pandas as pd
num_inputs = int(input("Enter Number For Range : "))        #It takes input number of to be entered in the series
user_inputs = []                                            #This empty list contains user inputs numbers
sqr=[]                                                      #This empty list contains Square of each elements
for i in range(1,num_inputs+1):
    num = int(input(f"Enter A Number {i} : "))              #Taking inputs from user as each element in the series
    if(num<=0):
        print("Note: Please Enter Only Postive Numbers")
        break
    else:
        user_inputs.append(num)                              #Appending all the inputs to empty list (user_inputs)
        sqr.append(num*num)                                  #Appending all the Squares of each element in the series
result = pd.Series(sqr, index=[user_inputs])
print(f"Square Of All The Inputs : \n{result}")              #Printing Series In Proper Manner


