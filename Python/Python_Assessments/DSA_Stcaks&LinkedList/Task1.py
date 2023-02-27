'''
Write a program to create a function that takes two sorted linked lists in ascending order as input and returns a sorted linked list in ascending order. 

Input:
    list1= 2->1->3
    list2=4->6->5

Output :  sortedlist = 1->2->3->4->5->6

Note - Don’t use any in-built functions
'''

#Creating Class Node
class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Function to create newNode in a linkedlist
def newNode( key):
	temp = Node(key)
	temp.data = key
	temp.next = None
	return temp

# A function to print linked list
def printList( node):
	while (node != None):
		print(node.data, end = " ")
		node = node.next

# Merges two given lists in-place.
# This function mainly compares head nodes and calls merge())
def merge( h1, h2):
	if (h1 == None):
		return h2
	if (h2 == None):
		return h1

	# start with the linked list
	# whose head data is the least
	if (h1.data < h2.data):
		h1.next = merge(h1.next, h2)
		return h1
	
	else:
		h2.next = merge(h1, h2.next)
		return h2
	
#List _1
head1 = newNode(2)
head1.next = newNode(4)
head1.next.next = newNode(6)


# List_2
head2 = newNode(1)
head2.next = newNode(3)
head2.next.next = newNode(5)
head1.next.next.next = newNode(7)


# Sorting and merging two linkedlist
mergedhead = merge(head1, head2)
#printing sorted linkedlist
print("Sorted LinkedList")
printList(mergedhead) 