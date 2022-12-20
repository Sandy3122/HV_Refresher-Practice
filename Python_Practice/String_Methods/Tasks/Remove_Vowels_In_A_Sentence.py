#Remove Vowels In A String
#Input :
# Hello World

#Output String :
# Hll Wrld


input_str = input("Enter A String : ")
input_str.split()
print(input_str)
vowels = ('a', 'e', 'i', 'o', 'u')

for i in input_str:
    if(i.lower() in vowels):
        input_str = input_str.replace(i,"")
print(input_str)