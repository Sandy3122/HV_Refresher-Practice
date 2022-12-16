''' 
#Given a word, write a program to convert all the uppercase letters to lowercase letters and vice versa

Sample Input : "Coding"

Sample Output : "cODING"

'''
#########
# Case_1
#########

# word = input("Enter Any String With Atleast One UpperCase Letter : ")
# new_word=""
# if word.isupper():
#     print(word.lower())
# else:
#     for i in word:
#         if (i.isupper()):
#             new_word+=i.lower()
#         else:
#             new_word+=i.upper()
#     print(new_word)


#########
#  OR   #
#########
word = input("Enter Any String With Atleast One UpperCase Letter : ")
new_word=""
for i in word:
    if (i.isupper()):
        new_word+=i.lower()
    elif(i.islower()):
        new_word+=i.upper()
print(new_word)



#########
# Case_2
#########
#By Using Built In Function

# word = input("Enter Any String With Atleast One UpperCase Letter : ")
# print(word.swapcase())
