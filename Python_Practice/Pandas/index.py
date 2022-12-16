#Index Concept 

import pandas as pd
# a = [1,2,3]
# myvar = pd.Series(a, index=["x","y","z"])
# print(myvar)

# a1 =[22,31,30,9]
# y = pd.Series(a1, index=["Geethu", "Taruni", "Daddy", "Amma"])
# print(y)

#########
## Taking Student Name And Marks
#########
data=open("studentDetails.txt", "a")
studentName=[input("Enter Student Names : ") for _ in range(5)]
marks=[int(input("Enter Student Marks : ")) for _ in range(5)]
z = pd.Series(marks, index=[studentName])
print(z)
print(f"Student Details With Names And Marks : \n{z} \n", file=data)