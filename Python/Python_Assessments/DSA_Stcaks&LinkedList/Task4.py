'''
Create a program to implement Stack by using one queue. It allows the user to perform Push and Pop operations on it.

Sample -

What would you like to do? push 3

What would you like to do? push 5

What would you like to do? pop

Popped value:  5

What would you like to do? pop

Popped value:  3

What would you like to do? pop

Stack is empty.

'''

class Stack:
    def __init__(self):
        self.queue = []

    def isEmpty(self):
        return len(self.queue) == 0

    def Push(self, item):
        self.queue.append(item)
        for i in range(len(self.queue)-1):
            self.queue.append(self.queue.Pop(0))

    def Pop(self):
        if self.isEmpty():
            return None
        return self.queue.Pop(0)

    def Show(self):
        if self.isEmpty():
            print("Stack is empty.")
        else:
            print("Stack: ", self.queue)

Stack = Stack()

while True:
    print('\n',"Push", '\n', "Pop", '\n', "Show", '\n', "Exit" )
    userInput = input("Please enter your option from above: ")

    if userInput == "Push":
        item = int(input("Enter item to be pushed: "))
        Stack.Push(item)
        print("Your Item is pushed into Stack.")
        
    elif userInput == "Pop":
        item = Stack.Pop()
        if item is None:
            print("Your Stack is empty.")
        else:
            print("Popped item from the Stack : ", item)
            
    elif userInput == "Show":
        Stack.Show()
        
    elif userInput == "Exit":
        break
    
    else:
        print("Please select valid option and try again.")