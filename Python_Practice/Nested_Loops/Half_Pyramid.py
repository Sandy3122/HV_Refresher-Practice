#Half Pyramid

#For Input 4
# Brutt Force Case 
'''
N = int(input("Enter A Number : "))

row_num = ""
for i in range(1, 2):
    row_num = row_num + str(i) + " "
print (row_num)

row_num = ""
for i in range(1, 3):
    row_num = row_num + str(i) + " "
print (row_num)

row_num = ""
for i in range(1, 4):
    row_num = row_num + str(i) + " "
print (row_num)

row_num = ""
for i in range(1, 5):
    row_num = row_num + str(i) + " "
print (row_num)

'''

#Best Case

N = int(input("Enter A Number : "))
for i in range(1, N+1):
    row_num = ""
    for j in range(1, i+1):
        row_num = row_num + str(j) + " "
    print (row_num)