#Armstrong Number For Number 3 Digit Number
############
## Case 1 ##
############

# n=int(input("enter a number. : "))
# total =0
# temp = n
# while(n!=0):
#     nw=n%10
#     total = nw*nw*nw + total
#     n=n//10
# print(total)    
# if(temp == total):
#     print("Armstrong number")
# else:
#     print("not an armstrong number")      


############
## Case 2 ##
############

# num = int(input("Enter A Number : "))
# sum = 0
# temp = num
# while (temp > 0):
#     digit = temp % 10       # TO Get Reminder
#     # print(digit)
#     sum += digit**3
#     # print(sum)
#     temp =temp//10
#     # print(temp)
# if(num == sum):
#     print("Number Is An Armstrong Number")
# else:
#     print("Number Is Not An Armstong Number")



############
## Case 3 ##
############

# num = int(input("Enter A Number : "))
# sum = 0
# temp = num
# len_num = len(str(num))
# while (temp > 0):
#     digit = temp % 10       # TO Get Reminder
#     # print(digit)
#     sum += digit**len_num
#     # print(sum)
#     temp =temp//10
#     # print(temp)
# if(num == sum):
#     print("Number Is An Armstrong Number")
# else:
#     print("Number Is Not An Armstong Number")



############
## Case 4 ##
############
#This Program Is Only To Check Three Digits ArmStrong Number

num = int(input("Enter A Number : "))
sum = 0
temp = num
input_lst, sum_lst, ind_lst = [] , [] , []
len_num = len(str(num))
while (temp > 0):
    digit = temp % 10       # TO Get Reminder
    input_lst.append(digit)
    sum += digit**len_num
    sum_lst.append(sum)
    temp =temp//10
    ind_lst.append(temp)
if(num == sum):
    # print(f"{input_lst}\n{sum_lst}\n{ind_lst}")
    print(f"Proof : {input_lst[2]}**{len_num} = {input_lst[2]**len_num} + {input_lst[1]}**{len_num} = {input_lst[1]**len_num} + {input_lst[0]}**{len_num} = {input_lst[0]**len_num} => {sum_lst[-1]}")
    print(f"{num} == {sum}")
    print("Number Is An Armstrong Number")
else:
    print(f"Proof : {input_lst[2]}**{len_num} = {input_lst[2]**len_num} + {input_lst[1]}**{len_num} = {input_lst[1]**len_num} + {input_lst[0]}**{len_num} = {input_lst[0]**len_num} => {sum_lst[-1]}")
    print(f"{num} != {sum}")
    print("Number Is Not An Armstong Number")