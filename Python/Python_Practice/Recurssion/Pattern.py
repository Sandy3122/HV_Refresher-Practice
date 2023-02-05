






# n = int(input("Enter No.of Entries : "))
# for i in range(n, 0, -1):
# #    print((n-1) * ' ' + i * ' *')
#    print(i * ' * ' + (n-1) * ' ' )





# Print The Below Pattern

#   1
#  123
# 12345
#  123
#   1


rows = int(input("Enter No.of Entries : "))
for i in range(1, rows + 1):
    for j in range(1, rows - i + 1):
        print(end=' ')
    for k in range(1, (2*i)):
        print(k, end="")
    print()
for i in range(rows - 1, 0, -1):
    for j in range(1, rows - i + 1):
        print(end=' ')
    for k in range(1, (2*i)):
        print(k, end="")
    print()
