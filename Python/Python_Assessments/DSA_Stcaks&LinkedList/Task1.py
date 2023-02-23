'''
Write a program to create a function that takes two sorted linked lists in ascending order as input and returns a sorted linked list in ascending order. 

Input:
    list1= 2->1->3
    list2=4->6->5

Output :  sortedlist = 1->2->3->4->5->6

Note - Don’t use any in-built functions
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None   