#swapping first and last elements in a list
a = []
n = int(input("Number of elements in list: "))
for x in range(0, n):
    element = int(input("Enter the element " +str(x+1) +": "))
    a.append(element)
temp = a[0]
a[0] = a[n-1]
a[n-1] = temp
print("New list is: ", a)
first = a[0]**2
last = a[n-1]**2
print("square of first is: ",first)
print("square of last is: ",last)
print("sum of first and last is:", (first+last))






