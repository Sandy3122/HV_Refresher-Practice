def selection_sort(arr):     #creating a function selection_sort with single argument
    for i in range(0, len(arr-1)):  #create a loop with a loop variable i which start from 0 till arr -1
        min=i  # now take the variable min and assign i to it
        for j in range(i+1, len(arr)):
            # create a inner loop with a variable j that start from i+1 till arr-1
            if(arr[j]<=arr[min]):  
                 # if the elements at index j is smaller or equal to the elements index min ,than set min equal j
                min=j
        arr[i],arr[min]=arr[min],arr[i]
        # swap the elements at indices i and min
arr=input("Enter the numbers:").split()
arr=[int(x) for x in arr]
selection_sort(arr)
print("sorted list is:",arr)