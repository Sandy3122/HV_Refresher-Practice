#write a program to execute the mergesort

# 1. Create a function merge_sort that takes a list and two variables start and end as arguments.
# 2. The function merge_sort will sort the list from indexes start to end – 1 inclusive.
# 3. If end – start is not greater than 1, then return.
# 4. Otherwise, set mid equal to the floor of (start + end)/2.
# 5. Call merge_sort with the same list and with start = start and end = mid as arguments.
# 6. Call merge_sort with the same list and with start = mid and end = end as arguments.
# 7. Call the function merge_list, passing the list and the variables start, mid and end as arguments.
# 8. The function merge_list takes a list and three numbers, start, mid and end as arguments and assuming the list is 
# sorted from indexes start to mid – 1 and from mid to end – 1, merges them to create a new sorted list from indexes start to end – 1.

def Merge_sort(alist, start, end):
    if end-start > 1:
        mid = (start+end)//2
        Merge_sort(alist,start,mid)
        Merge_sort(alist, mid, end)
        Merge_list(alist, start, mid, end)

def Merge_list(alist, start, mid, end):
    left = alist[start:mid]
    right = alist[mid:end]
    k = start
    i = 0
    j = 0
    while (start+i < mid and mid+j < end):
        if (left[i] <= right[j]):
            alist[k] = left[i]
            i= i+1
        else:
            alist[k] = right[j]
            j= j+1
        k = k+1
    if (start + i < mid):
        while (k < end):
            alist[k] = left[i]
            i= i+1
            k = k+1
    else:
        while (k < end):
            alist[k] = right[j]
            j= j+1
            k= k+1

alist = input("Enter the numbers: ").split()
alist = [int(x) for x in alist]
Merge_sort(alist, 0, len(alist))
print("Sorted list is: ", alist)






# For String As Input #
# def Merge_sort(alist, start, end):
#     if end-start > 1:
#         mid = (start+end)/2
#         Merge_sort(alist,start,mid)
#         Merge_sort(alist, mid, end)
#         Merge_list(alist, start, mid, end)

# def Merge_list(alist, start, mid, end):
#     left = alist[start:mid]
#     right = alist[mid:end]
#     k = start
#     i = 0
#     j = 0
#     while (start+i < mid and mid+j < end):
#         if (left[i] <= right[j]):
#             alist[k] = left[i]
#             i= i+1
#         else:
#             alist[k] = right[j]
#             j= j+1
#         k = k+1
#     if (start + i < mid):
#         while (k < end):
#             alist[k] = left[i]
#             i= i+1
#             k = k+1
#     else:
#         while (k < end):
#             alist[k] = right[j]
#             j= j+1
#             k= k+1

# alist = input("Enter The Names: ").split()
# Merge_sort(alist, 0, len(alist))
# print("Sorted list is: ", alist)