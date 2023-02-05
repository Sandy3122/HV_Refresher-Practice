#Student height - Go through each student and find the tallest student and put him/her at the end.

def student_height(arr):
    for i in range(0, len(arr)-1):
        min=i
        for j in range(i+1, len(arr)):
            if(arr[j] <= arr[min]):
                min=j
        arr[i],arr[min] = arr[min],arr[i]
        print(arr)
try:
    arr=list(map(float,input("Enter The Student Heights In Feet: ").split()))
    student_height(arr)
    print("Sorted Studnet Height",end='')
    print(arr)
except ValueError:
    print("Enter Student Heights In Integers Only!")


# A 2 3 4 5 6 7 8 9 10 K Q J

