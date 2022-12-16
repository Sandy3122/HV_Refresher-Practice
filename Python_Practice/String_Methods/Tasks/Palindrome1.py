#Checking Weather Given String Is Palindrome Or Not
#Note : Ignoring all the uppercase and lowercase
def reverse_str(s):
    new = s.upper()
    print(new)
    new_str=""
    check1 = True
    check2 = False
    for i in new:
        new_str = i + new_str
    print(new_str)
    if new_str == new:
        return check1
    else:
        return check2
s = input()
print(reverse_str(s))