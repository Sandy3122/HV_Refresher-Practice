check = input("Enter the filename: ")
k = 0
with open(check,'r') as x:
    for line in x:
        words = line.split()
        for i in words:
            for letter in i:
                if (letter.isspace()):
                    k=k+1

print("Number of spaces: ",k)