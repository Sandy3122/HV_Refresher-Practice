''' 
# Sorting Using Built In Function

data = list(map(int, input().split()))

sorted_Data = sorted(data)

print(sorted_Data)
'''


# Sorting In using Logic

myData = list(map(int, input("Enter Numbers Using Space : ").split()))

for i in range(len(myData)):
    for j in range(i+1, len(myData)):
        if(myData[i] > myData[j]):
            myData[i], myData[j] = myData[j], myData[i]     #Swapping

print(f"Sorted List : {myData}")