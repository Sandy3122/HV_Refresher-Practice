#Find The given input is a LowerCase Letter or UpperCase Letter or Digit Or A Special Character

char = input("Enter A Character : ")
for i in char:
    if(i.isnumeric()):
        print("Digit")
    elif(i.isalpha() and i.islower()):
        print("Lowercase Letter")
    elif(i.isalpha() and i.isupper()):
        print("Uppercase Letter")
    else:
        print("Special Character")