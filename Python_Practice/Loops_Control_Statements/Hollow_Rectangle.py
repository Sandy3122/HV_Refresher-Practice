''''
Given 2 integers M And N, write a program to print a hollow reactangle pattern
of M rows And N columns using asterisk character ( * ).

M And N Are Positive Integers

'''


M = int(input())                #For Rows
N = int(input())                #For Columns
for i in range(1, M+1):         #For Row Iteration
    for j in range(1, N+1):     #For Column Iteration
        if(i == 1 or i == M or j == 1 or j == N):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()                     #For Every i Iteration It Will Go Into New Line