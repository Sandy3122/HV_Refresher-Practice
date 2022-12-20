def reverse_list(arr):
    left = 0
    right = len(arr)-1
    while(left < right):
        temp = arr[left]
        arr[left] = arr[right]
        arr[right] = temp
        left += 1
        right -= 1
    return arr
# arr = list(map(int, input("Enter Numbers In The List : ").split()))
num = int(input("Enter, how Many Entries You Want : "))
arr = [int(input(f"Enter {x} Number : ")) for x in range(1, num+1)]
print(arr)
print(reverse_list(arr))
