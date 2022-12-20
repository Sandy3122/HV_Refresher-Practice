'''
Check Sum Of Digits Is Palindrome Or Not

Given a number N. Find if the digit sum (or sum of digits) of N is a Palindrome number or not. If

INPUT 
N = 56
Output
1

Explanation
The digit sum of 56 is 5+6 = 11
Since, 11 is a Palindrome Number, Thus, Number Is 1.

Ex : 1 569
1+5+6+9 = 21
21 != 12

'''
############
## Case_1 ##
############

def isPalindrome(N): 
    newNum = 0
    while(N > 0): 
        newNum += N % 10
        N = N // 10
    revNewNum = 0
    N = newNum
    while(N > 0):
        revNewNum = revNewNum * 10 + N % 10
        N = N // 10
    return 1 if(revNewNum == newNum) else 0
N = int(input("Enter A Number : "))
print(isPalindrome(N))



############
## Case_2 ##
############

num = int(input("Enter A Number : "))
lst = [int(i) for i in range(num)]


