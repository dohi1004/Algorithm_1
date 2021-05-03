#!/usr/bin/env python
# coding: utf-8

# 스택 Min : 기본적인 push 기능과 pop 기능이 구현된 스택에서 최솟값을 반환하는 min 함수를 추가하려고 한다. 어떻게 설계할 수 있겠는가? push, pop, min 연산은 모두 O(1) 시간에 동작해야 한다.

# In[40]:


class stack:
    def __init__(self):
        self.stack = []
        self.minstack = []
    def push(self,val):
        if len(self.stack) == 0:
            self.minstack.append(val)
        else:
            # 제일 최소를 뽑는 거니까 제일 낮았던 애랑만 비교하면 됨(제일 위의 값과 새로들어오는 값 비교)
            # 제일 낮은 애를 제일 위로 올려
            if(val > self.minstack[-1]):
                temp = self.minstack.pop()
                self.minstack.append(val)
                self.minstack.append(temp)
            else:
                self.minstack.append(val)
        self.stack.append(val)
        
    def pop(self):
        if len(self.stack) != 0:
            temp = self.stack.pop()
            # 실제 stack에서 지워진 값을 minstack에서 지움
            self.minstack.remove(temp)

        else:
            print("no value in stack")
        
    def min(self):
        return self.minstack[-1]
    
    # test
    def print(self):
        print(self.stack)
        print(self.minstack)
            
   
top = stack()
top.push(1)
top.push(5)
top.push(3)
top.pop()
top.push(9)
top.push(0)
top.push(10)
top.print()
top.min()

