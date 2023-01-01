#Leap Year

year = int(input("Enter The Year : "))
if((year%100 == 0 and year%100 == 0) and (year%4 == 0 and year%100 != 0)):
    print("{0} Is The Leap Year ".format(year))
else:
    print("{0} Is Not A Leap Year ".format(year))
