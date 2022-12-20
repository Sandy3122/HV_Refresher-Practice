#Swapping First Index And last Index

# def swap_list(lst):
#     temp = lst[0]
#     lst[0] = lst[-1]
#     lst[-1] = temp
#     return  lst

def swap_list(lst):
    lst[0] , lst[-1] = lst[-1], lst[0]
    return  lst

num = int(input("Enter The Range Of List : "))
lst = [int(input(f"Enter {i} Number : ")) for i in range(1, num+1)]
print(lst)
print(swap_list(lst))