#Selection Sort


def selection_sort(arr):
    for i in range(0, len(arr)-1):
        min = i
        for j in range(i+1, len(arr)):
            if(arr[j] <= arr[min]):
                arr[j], arr[min] = arr[min], arr[j]
        print(arr)
        
userInput = int(input("ENter Number Of To Enter : "))
arr = [int(input(f"Enter {_} Number : ")) for _ in range(1, userInput+1)]
selection_sort(arr)
print("Sorted Array : ", '\n',arr)