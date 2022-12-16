#Checking Weather Given String Is Palindrome Or Not
#Note : Treating uppercase and lowercase as same when comparing letters and ignore spaces and quotes within the string will string

def reverse_str(s):
    new_word = s.replace("'","")
    new_word = new_word.replace(" ","")
    uppercse=new_word.upper()
    reverse_word = ""
    for i in uppercse:
        reverse_word = i + reverse_word
    if reverse_word == uppercse:
        return True
    else:
        return False

s = input("Enter Any String : ")
print(reverse_str(s))

##########
##  OR  ##
##########

# def reverse_str(s):
#     s = s.replace("'","")
#     s = s.replace(" ","")
#     uppercse=s.upper()
#     reverse_word = ""
#     for i in uppercse:
#         reverse_word = i + reverse_word
#     if reverse_word == uppercse:
#         return True
#     else:
#         return False
# s = input("Enter Any String : ")
# print(reverse_str(s))


# def reverse_str(s):
#     new_word = s.replace(" ","")
#     uppercase = new_word.upper()
#     reverse_word=""
#     for i in uppercase:
#         reverse_word = i + reverse_word
#     if reverse_word == uppercase:
#         return True
#     else:
#         return False
# s = input()
# print(reverse_str(s))