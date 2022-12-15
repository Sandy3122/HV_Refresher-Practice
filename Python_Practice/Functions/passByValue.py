def changeNumber(myList):                       #parametrized function(parameter: myList)
    myList.append([22,31,9,30])                 #[10, 12, 5, 30, [22, 31, 9, 30]]
    print('Values Inside The Function', myList)
    return
    
myList=[10,12,5,30]
print('Values Outside The Function', myList)    #[10, 12, 5, 30]
changeNumber(myList)