# Bubblesort one of the sorting technique where we are compare with the first value and second value,second value with third value and so on
# 1.create a function bubble sort at takes array as an argument
def Bubble_Sort(arr):
# 2.inside the function will create a loop with the loop variable at this i with will count array-1 to one
    for i in range(len(arr)-1,0,-1):
        noswap=True
# 3. create a inner loop at count 0 till i
        for j in range(0,i):
# 4. inside the inner loop if the elements at indices j and j+1 are out of order than swap them
            if(arr[j+1]<arr[j]):
                arr[j],arr[j+1]=arr[j+1],arr[j]
                noswap=False
        if noswap:
            return
        
# 5.if any of the iteration in the inner loop then their any wont be any swap,the list is sorted
arr=input("Enter the numbers:").split()
arr=[int(x) for x in arr]
Bubble_Sort(arr)
print("sorted list is:",arr)
