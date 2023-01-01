'''Create a dictionary in python with the name "Car", Which has keys and values. Fetch the "Brandname" as the key and "Color" as the value from the user.
Display the complete dictionary in the console and try to save the output in file. (Using the file handling concept)'''

Cars = {}                                                           #Created Empty Dictionary
data = open("task2Data.txt", "a")                                   #Appending User Data Into task@Data.txt
num = int(input("Enter Number Of Car Details To Be Entered: "))     #User Input for number of car details to enter
for i in range(num):
    brandName = input("Enter Car Brand Name: ")
    carColor = input("Enter Car Color: ")
    Cars[brandName] = carColor
print(Cars)
print("User Car Details: ",Cars, "\n","\n", file=data)              #Saving the user inputs in file