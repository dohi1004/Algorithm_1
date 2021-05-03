#!/usr/bin/env python
# coding: utf-8

# 2) 스택으로 큐 : 스택 두 개로 큐 하나를 구현한 MyQueue 클래스를 구현하라.

# In[43]:


class stack:
    def __init__(self):
        self.stack = []
        
    def push(self,val):
        self.stack.append(val)
        
    def pop(self):
        if(len(self.stack) != 0):
            return self.stack.pop()
        else:
            print("no value in stack(pop isn't available)")
            
    def isEmpty(self):
        if(len(self.stack) == 0):
            return True
        else:
            return False
    def test(self):
        print(self.stack)
        
    def size(self):
        return len(self.stack)
    
class MyQueue:
    def __init__(self):
        self.stack1 = stack()
        self.stack2 = stack()
    
    # 첫 번째 스택에 값 다 넣기
    def enqueue(self,val):
        self.stack1.push(val)
    
    def dequeue(self):
        if(self.stack2.isEmpty()):
            size1 = self.stack1.size()
            #  stack1이 빌 때 까지 stack2로 값 옮기기
            while self.stack1.isEmpty() is False:
                temp = self.stack1.pop()
                self.stack2.push(temp)
        # stack2의 제일 위에 값 return(pop)
        return self.stack2.pop()
    
    def print(self):
        print("stack1")
        self.stack1.test()
        print("stack2")
        self.stack2.test()
        
queue = MyQueue()
print("**enqueue test**")
# 첫번째 스택에 차례대로 넣음
queue.enqueue(1)
queue.enqueue(3)
queue.enqueue(2)
queue.print()
print("**dequeue test**")
# 2번째 스택으로 옮긴 후 제일 위에거 pop하면 queue와 같이 동작함
# 제일 앞에 1 나간거 확인 가능!
queue.dequeue()
queue.print()

