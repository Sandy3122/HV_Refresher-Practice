#Word Triangle
#Input :
# ABCD

#Output :
# A
# AB
# ABC
# ABCD

input_str = input("Enter A String : ")
sub_str = ''
for i in input_str:
    sub_str += i
    print(sub_str)