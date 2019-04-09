#!/usr/bin/env python

'''Linked List implementation in Python

Base Node and UnorderedList classes pulled from:
interactivepython.org/runestone/static/pythonds/BasicDS/ImplementinganUnorderedListLinkedLists.html

'''

class Node:

    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def getPrev(self):
        return self.prev
    
    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def setPrev(self, newprev):
        self.prev = newprev
        
class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def printList(self):
        current = self.head

        print('(', end = '')
        
        while current != None:
            print(current.getData(), end = '')
            current = current.getNext()
            if current != None:
                print(',', end = '')
        print(')')

    def printData(self, item):
        
        nextItem = item.getNext()
        if nextItem == None:
            nextItem = 'None'
        else:
            nextItem = nextItem.getData()
            
        print('Item: {}, Next: {}'.format(item.getData(), nextItem))

    def printAllData(self):
        current = self.head

        while current != None:
            self.printData(current)
            current = current.getNext()
        
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
    
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

class DoublyLinkedList(UnorderedList):

    def printData(self, item):
        
        nextItem = item.getNext()
        prevItem = item.getPrev()
        
        if nextItem == None:
            nextItem = 'None'
        else:
            nextItem = nextItem.getData()

        if prevItem == None:
            prevItem = 'None'
        else:
            prevItem = prevItem.getData()

        print('Item: {}, Next: {}, Previous: {}'.format(item.getData(), nextItem, prevItem))

    def printAllData(self):
        current = self.head

        while current != None:
            self.printData(current)
            current = current.getNext()
        
    def add(self, newdata):
        temp = Node(newdata)
        if self.head != None:
            self.head.setPrev(temp)
        temp.setNext(self.head)
        self.head = temp

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
            self.head.setPrev(None)
        else:
            previous.setNext(current.getNext())
            current.getNext().setPrev(previous)
                
        
if __name__ == '__main__':
    singly = UnorderedList()
    singly.add(93)
    singly.add(35)
    singly.add(45)
    singly.add(101)
    singly.printList()
    singly.add(36)
    singly.add(38)
    singly.remove(101)
    singly.printList()
    singly.printAllData()
    print()

    doubly = DoublyLinkedList()
    doubly.add(12)
    doubly.add(53)
    doubly.add(72)
    doubly.printList()
    doubly.remove(53)
    doubly.add(87)
    doubly.add(34)
    doubly.printList()
    doubly.printAllData()
