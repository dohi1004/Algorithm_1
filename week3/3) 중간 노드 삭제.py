#!/usr/bin/env python
# coding: utf-8

# 3) 중간 노드 삭제 :  단방향 연결리스트가 주어졌을 때, 중간(처음과 끝 노드 제외)노드 하나를 삭제하는 알고리즘을 구현하라.
#         입력 : 연결리스트드 a->b->c->d->e 에서 노드 c
#         결과 :  a->b->d->e

# In[21]:


class Node(object):
    def __init__(self,data):
        self.data = data
        self.next = None

class SinglyLinkedList(object):
    def __init__(self):
        self.head = Node(None)
        self.size = 0
        
    def append(self, val):
        current = self.head
        while current.next is not None:
            current = current.next
        current.next = Node(val)
    
    def printlist(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
            
    def deletemiddle(self, val):
        current = self.head
        temp = self.head
        while current is not None:
            if(current.data == val):
                break
            temp = current
            current = current.next
        temp.next = current.next

        
        
obj = SinglyLinkedList()
obj.append('a')
obj.append('b')
obj.append('c')
obj.append('d')
obj.append('e')
obj.deletemiddle('c')
obj.printlist()

