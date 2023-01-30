# How the contact list on your phone is sorted in alphabetical order

#Bubble Sort

def contactlist(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if ord(arr[j][0]) > ord(arr[j+1][0]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
        print(arr)

arr = list(input("Enter The Names : ").split())
contactlist(arr)

print("Sorted Contact List :")
for i in range(len(arr)):
    print(arr[i])