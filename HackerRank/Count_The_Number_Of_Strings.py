'''
Write a Python program to count the number of strings where the string length is 2 or more
and the first and last character are same from a given list of strings.

'''
def string_count(words):
    count = 0
    for i in words:
        if(len(i) > 1 and i[0] == i[-1]):
            count += 1
    return count

num = int(input("ENter The Number : "))
words = [input(f"Enter {_} String : ") for _ in range(1,num+1)]
print(string_count(words))

#Input
# aba
# abc
# abd
# sfd
# asj
# Ans = 1