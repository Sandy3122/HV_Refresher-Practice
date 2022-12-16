#Checking Weather The Pin Is ( digit and length is 4 )

pin = "3122"
# pin = "312o"
is_digit = pin.isdigit()        #Gives Boolean Value ( True )
print(is_digit)
is_4_digit = (len(pin) == 4)    #Gives Boolean Value ( True )
is_valid = (is_digit and is_4_digit)    #Gives Boolean Value ( True And True )
print(type(is_valid))
print(is_valid)