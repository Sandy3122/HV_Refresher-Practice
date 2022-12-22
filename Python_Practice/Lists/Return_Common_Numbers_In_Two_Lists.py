#Write a Python function that takes two lists 
#and returns True if they have at least one common member.


def common_num(lst1, lst2):
    result = False
    count = 0
    for i in lst1:
        for j in lst2:
            if i == j:
                result = True
                count += 1
    return (result, count)

num = int(input())
lst1 = [int(input(f"Enter {1} Number In First List : ")) for _ in range(1,num+1)]
lst2 = [int(input(f"Enter {1} Number In Second List : ")) for _ in range(1,num+1)]
print(common_num(lst1, lst2))