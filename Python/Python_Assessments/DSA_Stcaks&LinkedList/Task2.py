'''
Create a program that allows users to enter customer data.

The customer data should include the following information:

    Customer Id
    Customer Name
    Purchase date(dd/mm/yy)
    Bill amount

Store this information in a linked list. The program should provcustIde three options for viewing information:

    View all customer data in sorted order based on bill amount
    View the total purchase amount for a specific year
    View details of a specific customer based on name

'''

# Importing datetime
import datetime


class Customer:
    def __init__(self, custId, custName, Date, Amount):
        self.custId = custId
        self.custName = custName
        self.Date = datetime.datetime.strptime(Date, '%d/%m/%y')
        self.Amount = Amount
        self.next = None  

class LinkedList:
    def __init__(self):
        self.head = None

    def customer(self, custId, custName, Date, Amount):
        new_customer = Customer(custId, custName, Date, Amount)
        if self.head is None:
            self.head = new_customer
        else:
            currentHead = self.head
            while currentHead:
                if currentHead.Amount >= new_customer.Amount:
                    if currentHead == self.head:
                        new_customer.next = self.head
                        self.head = new_customer
                    else:
                        new_customer.next = currentHead
                        previous.next = new_customer
                    break
                elif currentHead.next is None:
                    currentHead.next = new_customer
                    break
                previous = currentHead
                currentHead = currentHead.next


    def viewCustomers(self):
        currentHead = self.head
        while currentHead:
            print(f'Customer custID: {currentHead.custId}')
            print(f'Customer custName: {currentHead.custName}')
            print(f'Purchase Date: {currentHead.Date.strftime("%d/%m/%y")}')
            print(f'Bill Amount: {currentHead.Amount}')
            print()
            currentHead = currentHead.next

    def viewTotalAmount(self, year):
        currentHead = self.head
        totalAmount = 0
        while currentHead:
            if currentHead.Date.year == year:
                totalAmount += currentHead.Amount
            currentHead = currentHead.next
        print(f'Total Purchase Amount for {year}: {totalAmount}')

    def customerDetails(self, custName):
        currentHead = self.head
        while currentHead:
            if currentHead.custName == custName:
                print(f'Customer custId: {currentHead.custId}')
                print(f'Purchase Date: {currentHead.Date.strftime("%d/%m/%y")}')
                print(f'Bill Amount: {currentHead.Amount}')
                break
            currentHead = currentHead.next
        else:
            print(f'{custNname} not found in customer list')


customerList = LinkedList()


while True:
    print('Enter customer details (or "done" to finish):')
    custId = input('Customer custId: ')
    if custId == 'done':
        break
    custName = input('Customer custName: ')
    Date = input('Purchase Date (dd/mm/yy): ')
    Amount = int(input('Bill Amount: '))
    customerList.customer(int(custId), custName, Date, Amount)


customerList.viewCustomers()


year = int(input("Enter 'Year' to view total purchase Amount: "))
customerList.viewTotalAmount(year)


custName = input("Enter 'Customer Name' to view details: ")
customerList.customerDetails(custName)