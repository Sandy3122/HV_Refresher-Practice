'''
Numbers In Square Patter

Intput :
5

Output : 
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5

'''

N = int(input())                #For Rows & Columns
for i in range(1, N+1):         #For Row Iteration
    for j in range(1, N+1):     #For Column Iteration
            print(i, end=" ")
    print()                     #For Every i Iteration It Will Go Into New Line