# Check Weather Given String Is a Palindrome Or Not
#Note : Ignore upper case and lower case

#############
# PROBLEM 1
#############
# word = input()
# upp_word = word.upper()
# rev_str = upp_word[::-1]
# if rev_str == upp_word:
#     print("Palindrome")
# else:
#     print("Not a Palindrome")


#############
# PROBLEM 2
#############
# Python code to reverse a string
# using reversed()
# Function to reverse a string

# def reverse(string):
#     string = "".join(reversed(string))
#     return string
  
# s = input("Enter A String To Check Weather It Is A Palindrome Or Not : ")
  
# print("The original string is : ", end="")
# print(s)
  
# print("The reversed string(using reversed()) is : ", end="")
# print(reverse(s))


#############
# PROBLEM 3
#############

# Function to reverse a string
# by converting string to list
# # then reversed it and again convert it to string

# def reverse(string):
#     string = list(string)
#     string.reverse()
#     return "".join(string)
  
# s = input("Enter A String To Check Weather It Is A Palindrome Or Not : ")
  
# print("The original string  is : ", s)
  
# print("The reversed string(using reversed) is : ", reverse(s))



#############
# PROBLEM 4
#############
# Using for loop
# Reverse String without using reverse function

# Define a function
def reverse_for(string):
    # Declare a string variable 
    rstring = ''

    # Iterate string with for loop
    for x in string:
        # Appending chars in reverse order
        rstring = x + rstring
    return rstring

string = 'Stechies'

# Print Original and Reverse string
print('Original String: ', string)
print('Reverse String: ', reverse_for(string))