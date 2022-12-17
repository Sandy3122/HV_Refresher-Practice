'''
Question 2 - 

Write a Python program on Series where the user will take some inputs, approx. 5 inputs and then it will display the power of all those inputs, taken in the first series. 


Sample Input - s1 -     1  4   5  6  9

Sample Output - s2 -  1  16  25  36  81
'''

import pandas as pd
num_inputs = int(input("Enter Number For Range : "))
user_inputs = []
sqr=[]
for i in range(num_inputs):
    num = int(input("Enter A Number : "))
    user_inputs.append(num)
    sqr.append(num*num)
result = pd.Series(sqr, index=[user_inputs])
print(f"Square Of All The Inputs : \n{result}")