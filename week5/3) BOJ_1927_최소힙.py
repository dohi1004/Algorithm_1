#!/usr/bin/env python
# coding: utf-8

# In[5]:


import heapq
import sys

start = int(input()) 
heap = []
num = int()
for i in range(start):
    num = int(sys.stdin.readline())
    if(num == 0):
        if(len(heap) == 0):
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,num)

