'''
Print Solid Diamond 
Input :
4

Output :
   *
  * *
 * * *
* * * *
 * * *
  * *
   *

Explanation :
####################################
# Considering 1st Half of Pyramid :
####################################
   *        i = 0
  * *       i = 1
 * * *      i = 2
* * * *     i = 3
No.of Spaces in each row = (N - i - 1)
i = 0 =>    4-0-1 = 3 
i = 1 =>    4-1-1 = 2
i = 2 =>    4-2-1 = 3
i = 3 =>    4-3-1 = 0

No.of *'s in each row = (i+1)
i = 0       0+1 = 1
i = 1       1+1 = 2
i = 2       2+1 = 3
i = 3       3+1 = 4

####################################
# Considering 2nd Half of Pyramid :
####################################

 * * *      i = 0
  * *       i = 1
   *        i = 2
No.of Spaces in each row = (i+1)
i = 0       0+1 = 1
i = 1       1+1 = 2
i = 2       2+1 = 3

No.of *'s in each row = (N - i - 1)
i = 0 =>    4-0-1 = 3 
i = 1 =>    4-1-1 = 2
i = 2 =>    4-2-1 = 3

'''

N = int(input("Enter A Number : "))
# 1st half Pyramind
for i in range(N):
    print(" " * (N-i-1) + "* " * (i+1))

# 2nd half Pyramind
for i in range(N-1):
    print(" " * (i+1) + "* " * (N-i-1))


# n = int(input())
# k = n-1
# for i in range(1, n+1):
#     spaces = " " * k
#     stars = "* " * i
#     print(spaces+stars)
#     k = k - 1