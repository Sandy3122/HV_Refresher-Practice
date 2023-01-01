'''
Given the first 2 terns A1 And A2 of an Arthematic Series. Find the Nth term of the Series.

Input
 
A1 = 2
A2 = 4
N = 4

Output
#8

Explanation
The Series is 2, 4, 6, 8, 10....
#The Nth term is 8

'''

def SeriesAP(A1, A2, N):
    difference = A2 - A1
    nTerm = A1+(N-1)*difference
    return nTerm

nTerm = SeriesAP(
A1 = int(input("Enter 1st Term : ")),
A2 = int(input("Enter 2nd Term : ")),
N = int(input("Enter Nth Term To Find : "))
)
print(f"The Nth Term In The Series : {nTerm}")


