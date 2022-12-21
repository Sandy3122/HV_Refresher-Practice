#Text Wrap

# input_str = input("Enter The String : ")
# width = int(input("Enter The Width : "))
# # input_str = list(input_str)
# print(input_str)
# len_str = len(input_str)
# for i in range(1,len_str+1):
#     res = input_str[:width]
#     print(res, end="\n")

#Without build-in textwrap module

# string, max_width = input(),int(input())
# for i in range(0, len(string), max_width):
#     print(i, end=' ')
#     print(string[i : i + max_width])

#With build-in textwrap module

import textwrap

def wrap(string, max_width):
    return textwrap.fill(string,max_width)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)