wordcount = input("Enter the file name :")
wordcheck= 0
with open(wordcount,'r') as x:
    for line in x:
        word = line.split()
        wordcheck+=len(word)
        
print("the total number of words are: ",wordcheck)
