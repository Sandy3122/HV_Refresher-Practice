'''
Question_1
Triangular Pattern With *""
Input :
 5
Output :
*
* *
* * *
* * * *
* * * * *
* * * * * *

'''
# N = int(input("Enter A Number : "))
# for i in range(0, N+1):
#     print("* "*(i+1) + " "*(N-i-1))


'''
Question_2
Triangular Pattern With *""
Input :
 5
Output :
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
'''

N= int(input("Enter A Number : "))
row_output = ""
for i in range(1, N+1):
    row_output = ""                     #For Every Iteration Of i raw_output is going to empty
    for j in range(1,i+1):
        row_output+=str(j) + " "        #Coverting j In string By using str()
    print(row_output)