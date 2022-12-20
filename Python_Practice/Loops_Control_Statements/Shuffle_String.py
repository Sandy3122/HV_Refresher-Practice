#Shuffle String

'''
Given a string S and N intergers, Where N is the length of the String S

Print the string after shuffling the characters as per the order of the integers given

#Input 
eimag
1
2
3
4
0

#Output
image

'''

input_str = input("Enter A String : ")
len_str = len(input_str)
shuffled_str = ""
for i in range(1,len_str+1):
    index = int(input("Enter Index in Order : "))
    shuffled_str += input_str[index]            #Concatinating The String
    print(shuffled_str)
print(shuffled_str)