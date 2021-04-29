#!/usr/bin/env python
# coding: utf-8

# In[11]:


class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None
        
class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.tail = None
        self.size = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        current = self.head
        for i in range(index):
            current = current.next
        if(current == None):
            return -1
        return current.data

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        newNode = Node(val)
        newNode.next = self.head
        self.head = newNode
        self.size += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        if self.head is None:
            self.addAtHead(val)
            
        else:
            newNode = Node(val)
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = newNode
            self.size += 1
            

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        
        if index < 0 or index > self.size: return
        if(index == 0):
            return self.addAtHead(val)
        if(index == self.size):
            return self.addAtTail(val)
        
        newNode = Node(val)
        current = self.head
        for i in range(index-1):
            current = current.next
        newNode.next = current.next
        current.next = newNode
        self.size += 1
            

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size: return
        self.size -= 1
        if(self.size == 0):
            self.head = None
            return
        if(index == 0):
            self.head = self.head.next
        else:
            current = self.head
            for i in range(index):
                temp = current
                current = current.next
            temp.next = current.next
        
# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

