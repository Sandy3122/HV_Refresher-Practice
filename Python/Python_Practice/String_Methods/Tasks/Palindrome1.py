#Checking Weather Given String Is Palindrome Or Not
#Note : Ignoring all the uppercase and lowercase
def reverse_str(s):
    new = s.upper()
    print(new)
    new_str=""
    for i in new:
        new_str = i + new_str
    print(new_str)
    if new_str == new:
        return True
    else:
        return False
s = input("Enter A String : ")
print(reverse_str(s))