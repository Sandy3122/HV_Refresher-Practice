# Find_Uppercase_Lowercase_in_a_string


input_str = input("Enter A String : ")
c1 = 0
c2 = 0
for i in input_str:
    if(i.islower()):
        c1 += 1
    elif(i.isupper()):
        c2 += 1
print(f"Lower Alphabets : {c1} ; Upper Alphabets : {c2}")
    