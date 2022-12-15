# Loops

# Task 
# Read an integer N. For all non-negative integers i < N, print i**2. See the sample for details.

# Input Format
# The first and only line contains the integer, N.

# Constraints
# 1 <= N <= 20

# Output Format
# Print N lines, one corresponding to each i.

# Enter your code here. Read input from STDIN. Print output to STDOUT


num = int(input("Enter A Number To Get Square Of Each Number : "))
if(num<=0):
    print("Note: Please Enter Positive Number > 0")
else:
    print("Sqaure Of Each Number In The Given Range: ")
    for i in range(num):
        print(i*i)
