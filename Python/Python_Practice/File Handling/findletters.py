check = input("Enter thr file name: ")
letter = input("Enther the letter: ")
k = 0
with open(check,'r') as x:
    for line in x:
        words= line.split()
        for i in words:
            for letter1 in i:
                if (letter1==letter):
                    k=k+1
print("number of letter occurence is: ",k)


#Find The Word In sampletext.txt file