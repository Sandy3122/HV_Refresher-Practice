'''
Create a program that allows users to enter customer data.

The customer data should include the following information:


Customer Id
Customer Name
Purchase date(dd/mm/yy)
Bill amount

Store this information in a linked list. The program should provide three options for viewing information:

View all customer data in sorted order based on bill amount
View the total purchase amount for a specific year
View details of a specific customer based on name
'''

class Stack:
    def __init__(self):
        self.Items = []
        self.MinimumItems = []

    def isEmpty(self):
        return len(self.Items) == 0

    def Push(self, item):
        self.Items.append(item)
        if len(self.MinimumItems) == 0 or item <= self.MinimumItems[-1]:
            self.MinimumItems.append(item)
            
    def Top(self):
        if not self.isEmpty():
            return self.Items[-1]
        
    def Pop(self):
        if not self.isEmpty():
            item = self.Items.Pop()
            if item == self.MinimumItems[-1]:
                self.MinimumItems.Pop()
            return item

    def Maximum(self):
        if not self.isEmpty():
            self.Items.sort()
            return self.Items[-1]
        
    def Minimum(self):
        if not self.isEmpty():
            return self.MinimumItems[-1]
        
    def Show(self):
        if self.isEmpty():
            print("Your Stack is empty.")
        else:
            for item in reversed(self.Items):
                print(item,end=" ")

Stack = Stack()

while True:
    print('\n',"Push", '\n', "Pop", '\n', "Top", '\n', "Max", '\n', "Min", '\n', "Show", '\n', "Exit" )
    userInput = input("Please enter your option from above: ")

    if userInput == "Push":
        item = int(input("Enter item to be pushed : "))
        Stack.Push(item)
        print("Your Item is pushed into Stack.")
        
    elif userInput == "Pop":
        item = Stack.Pop()
        if item is None:
            print("Your Stack is empty.")
        else:
            print("Popped item from the Stack : ", item)
            
    elif userInput == "Top":
        item = Stack.Top()
        if item is None:
            print("Your Stack is empty.")
        else:
            print("Top item from the Stcak: ", item)
            
    elif userInput == "Min":
        item = Stack.Minimum()
        if item is None:
            print("Your Stack is empty.")
        else:
            print("Minimum item in the stack: ", item)
            
    elif userInput == "Max":
        item = Stack.Maximum()
        if item is None:
            print("Your Stack is empty.")
        else:
            print("Maximum item in the stack: ", item)
            
    elif userInput == "Show":
        Stack.Show()
        
    elif userInput == "Exit":
        break
    
    else:
        print("Please select valid option and try again.")