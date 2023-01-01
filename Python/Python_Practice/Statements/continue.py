#Continue Statement

num = [2,4,6,8,10,12,14,16,18,20]
for i in num:
    print("Current Number: ", i)
    if(i>12):
        continue        #After satisfying the condition, it will continue the statement
    square = i*i
    print("Square of the number : ", square)
