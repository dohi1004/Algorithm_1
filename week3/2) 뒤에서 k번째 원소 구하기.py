#!/usr/bin/env python
# coding: utf-8

# 뒤에서 k번째 원소 구하기:  단방향 연결리스트가 주어졌을 때 뒤에서 k번째 원소를 찾는 알고리즘을 구현하라.

# In[8]:


class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.size = 0
        
    def addAtHead(self, val):
        newNode = Node(val)
        self.head = newNode
        self.size += 1 
        
    def findk(self,k):
        index = self.size-k
        current = self.head
        for i in range(index):
            current = current.next
        return current.data
        
obj = SinglyLinkedList()
obj.addAtHead(0)
obj.addAtHead(1)
obj.addAtHead(2)
obj.findk(3)

