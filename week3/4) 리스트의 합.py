#!/usr/bin/env python
# coding: utf-8

# 4) 리스트의 합 : 연결리스트로 숫자를 표현할 때 각 노드가 자릿수 하나를 가리키는 방식으로 표현할 수 있다. 각 숫자는 역순으로 배열되어 있는데, 첫 번째 자리수가 리스트의 맨 앞에 위치하도록 배열된다는 뜻이다. 이와 같은 방식으로 표현된 숫자 두 개가 있을 때, 이 두 수를 더하여 그 합을 연결리스트로 반환하는 함수를 작성하라.
#          입력 : (7->1->6) + (5->9->2). 즉, 617+295
#          결과 : 2->1->9 즉, 912.

# In[38]:


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
            if(current.data != None):
                print(current.data)
            current = current.next
            
    def addition(self):
        current = self.head
        first = ''
        while current is not None:
            if(current.data != None):
                first += str(current.data)
            current = current.next
        first = first[::-1]
        return first
    
        
# first input list      
obj = SinglyLinkedList()
obj.append('7')
obj.append('1')
obj.append('6')

# second input list
obj2 = SinglyLinkedList()
obj2.append('5')
obj2.append('9')
obj2.append('2')

# result of the addition
result = str(int(obj.addition()) + int(obj2.addition()))
result = result[::-1]

# make linked list again!
resultlist = SinglyLinkedList()
for i in range(len(result)):
    resultlist.append(result[i])
resultlist.printlist()

