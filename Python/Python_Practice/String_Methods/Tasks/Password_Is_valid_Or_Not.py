# Checking Password Is Valid Or Not...

# password = input("Enter A Password : ")
# if((password.isalpha()==True) or (password.isdigit()==True)):
#     print("Invalid Password")
# else:
#     print("Valid Password")



#########
#The problem statement, the password is considered to be valid if it contains at least one uppercase letter, one lowercase letter, and one digit.
#########
print("Paswoord Should Contain 1 UpperCase, 1 LowerCase, 1 Digit : ")
password = input("Enter A Password :")
contains_digit = False
for digit in password:
  is_digit = digit.isdigit()
  if is_digit:
    contains_digit = True
is_all_lower = (password.lower() == password)
# print(is_all_lower)
is_all_upper = (password.upper() == password)
# print(is_all_upper)
contains_lower_and_upper = (not is_all_lower) and (not is_all_upper)
# print(contains_lower_and_upper)
is_valid_password = (contains_digit and contains_lower_and_upper)
if is_valid_password:
  print("Valid Password")
else:
  print("Invalid Password")