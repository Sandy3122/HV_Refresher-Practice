
# Std1 = int(input("Enter Your Marks :"))
# Std2 = int(input("Enter Your Marks :"))
# Std3 = int(input("Enter Your Marks :"))
# Std4 = int(input("Enter Your Marks :"))
# Std5 = int(input("Enter Your Marks :"))
# marks = [Std1, Std2, Std3,Std4,Std5]

# n = int(input('Enter Number of students : '))
# marks = [int(input("Enter student marks")) for i in range(n)]

# for i in marks:
#     if(i<=40):
#         break
#     print('Marks of the students below 40: ', i)
# for i in marks:
#     if(i<=40):
#         print('Marks of the students < 40: ', i)
#         continue
#     print('Marks > 40: ', i)

# case2
lst = []
for i in range(5):
    marks = int(input("Enter Marks : "))
    if(marks <= 40):
        continue
    print('Marks > 40: ', marks)