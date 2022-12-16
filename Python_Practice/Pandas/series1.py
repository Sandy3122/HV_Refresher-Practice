# Checking the sugar for diabatics patient
import pandas as pd
data = open("BPDetails.txt", "a")
num_days = int(input("Enter A Number how Many Days You Want to Enter : "))
days = [input("Eneter The Day : ") for _ in range(num_days)]
ind_Bp = [int(input("Enter The BP In Numbers : ")) for _ in range(num_days)]
x = pd.Series(ind_Bp, index=[days])
print(x)
print(f"Patient BP Details With Respective Days : \n{x}\n\n", file=data)