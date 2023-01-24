check = input("Enter The File Name : ")
num_lines = 0
with open(check, 'r') as x:
    for line in x:
        num_lines+=1
        
print("Number Of Lines : ", num_lines)