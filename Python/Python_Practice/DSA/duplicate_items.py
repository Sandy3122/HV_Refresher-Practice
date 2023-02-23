#removeing duplicate elements in a list


a= []
n = int(input("Enter the number of elemnts: "))
for x in range(0, n):
    # element = int(input('Enter the element ' +str(x+1)+": "))
    element = int(input('Enter the element:'))
    a.append(element)
b = set()
unique = []
for x in a:
    if x not in b:
        unique.append(x)
        b.add(x)
print("Non duplicate elements: ", unique) 