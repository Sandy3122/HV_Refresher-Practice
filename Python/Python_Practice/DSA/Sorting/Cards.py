# sorting playing cards in your hands

def playing_cards(arr):
    for i in range(1,len(arr)):
        temp = arr[i]
        j=i-1
        while(j>=0 and temp<arr[j]):
            arr[j+1]=arr[j]
            j=j-1
        arr[j+1]=temp
try:
    arr=list(map(int,input("Enter The Card Number Between 2 to 10: ").split()))
    playing_cards(arr)
    print("Sorted Playing Cards",end='')
    print(arr)
except ValueError:
    print("Input only Integers!!!!")
    
