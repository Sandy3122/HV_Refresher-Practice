def insertion_Sort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while(j>=0 and temp<arr[j]):
            arr[j+1]=arr[j]
            j=j+1
        arr[j+1]=temp

arr=input("Enter the numbers").split()
arr=[int(x) for x in arr]
insertion_Sort(arr)
print("sorted list is",arr)