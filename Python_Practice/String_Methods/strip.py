# .strip() method
#The strip() method removes any leading (spaces at the beginning) and trailing (spaces at the end) characters (space is the default leading character to remove)
#By default it removes spaces

#Example_1
name = "   Sandeep    "
print(name)
print(name.strip())
num = "  7989175345  "
print(num)
print(num.strip())

#example_2
# for characters
my_name = "Sandeep."
print(my_name.strip('.'))       #rRemoves only ending "." characters
my_full_name = "Seeram.Sandeep."
print(my_full_name.strip("."))  #Removes Only Ending Or Begining Chars("."). It Won't Remove Middle Chars

# Example_3
name = "  ,, ... .. Sandeep,.. .. ,, "
print(name)
name = name.strip(",. ")    #Note: We have to assign to variable and in strip() we have include spaces and characters to be removed 
print(name)