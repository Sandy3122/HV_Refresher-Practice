# Find Vowels in the string


# input_str = input("Enter A String : ")
# vowels = 0
# for i in input_str:
#     if(i.lower() in 'aeiou'):
#         vowels += 1
#     elif(i.upper() in 'AEIOU'):
#         vowels += 1
# print(f"Number Of Vowels In A Given String {vowels}")


# input_str = input("Enter A String : ")
# vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
# count = 0
# for i in input_str:
#     if i in vowels:
#         count += 1
# print(f"Number Of Vowels In A Given String {count}")



input_str = input("Enter A String : ")
count = 0
for i in range(len(input_str)):
    if ((input_str[i] == "a")
        or (input_str[i] == "e")
        or (input_str[i] == "i")
        or (input_str[i] == "o")
        or (input_str[i] == "u")
        or (input_str[i] == "A")
        or (input_str[i] == "E")
        or (input_str[i] == "I")
        or (input_str[i] == "O")
        or (input_str[i] == "U")):
        count += 1
        
print(f"Number Of Vowels In A Given String {count}")