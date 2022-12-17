'''
Question 1 - 

Write a Python program on Series where we need to perform arithmetic operations (+, -, *,/, and %).
We can achieve this activity by using two Pandas series. 
While printing, first display both the series individually in the console and then show the results of the arithmetic operations.

'''

############
## Case_1 ##
###########
import pandas as pd                                                     #Importing Pandas As Pd
print("Arithmetic Operations (+, -, *,/, and %) On Two Series : ")
series1  = pd.Series([2,4,6,8,10])                                      #series1 is holding one-dimensional array
series2 = pd.Series([1,3,5,7,9])
print(f"First Series : \n{series1}")                                    #Printing series1
print(f"Second Series : \n{series2}")                                   #printing series2
print(f"Addition Of Two Series :\n{series1 + series2}")                 #Addition Of Two Series
print(f"Subtraction Of Two Series :\n{series1 - series2}")              #Subtraction Of Two Series
print(f"Multiplication Of Two Series :\n{series1 * series2}")           #Multiplication Of Two Series
print(f"Division Of Two Series :\n{series1 / series2}")                 #Division Of Two Series
print(f"Floor Division Of Two Series :\n{series1 // series2}")          #Floor Division Of Two Series


############
## Case_2 ##
############
# Taking Inputs From Users For Each Series

# import pandas as pd
# print("Arithmetic Operations (+, -, *,/, and %) On Two Series")
# elements_range = int(input("Enter Number Elemets To Be Taken In Each Series : "))
# series1 = pd.Series([int(input("Enter Number In First Series : ")) for _ in range(elements_range)])
# series2 = pd.Series([int(input("Enter Number In Second Series : ")) for _ in range(elements_range)])
# print(f"First Series : \n{series1}")
# print(f"Second Series : \n{series2}")
# print(f"Addition Of Two Series :\n{series1 + series2}")
# print(f"Subtraction Of Two Series :\n{series1 - series2}")
# print(f"Multiplication Of Two Series :\n{series1 * series2}")
# print(f"Division Of Two Series :\n{series1 / series2}")
# print(f"Floor Division Of Two Series :\n{series1 // series2}")