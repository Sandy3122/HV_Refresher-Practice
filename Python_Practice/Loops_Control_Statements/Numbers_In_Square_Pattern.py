'''
Numbers In Square Patter

Intput :
5

Output : 
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5

'''

N = int(input())                #For Rows & Columns
for i in range(1, N+1):         #For Row Iteration
    for j in range(1, N+1):     #For Column Iteration
            print(j, end=" ")
    print()                     #For Every i Iteration It Will Go Into New Line