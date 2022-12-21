'''
Inverted Half Pyramid_2

Input :
3

Output :
3 2 1
2 1
1
'''


#Best Case

N = int(input("Enter A Number : "))
for row_num in range(1,N+1):
    row_output = ""
    seq_num = N
    while seq_num > 0:
        row_output = row_output + str(seq_num) + " "
        seq_num = seq_num - 1
    N-=1
    print(row_output)