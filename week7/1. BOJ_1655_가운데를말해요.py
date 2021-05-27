#!/usr/bin/env python
# coding: utf-8

# ### 가운데를 말해요
# 
# 숫자가 들어왔을 때 현재 불러진 숫자들 중에서 중간 값을 뽑아내는 문제
# ex) 1 5 2 -> 1 1 2
# 
# 1 -> 1 // 1 5 -> 1 // 1 2 5 -> 2
# 
# 홀수 -> 가운데, 짝수 -> 가운데 두 수 중 더 작은 수
# 
# -> 두 힙을 이용하는데, 왼쪽은 max heap 오른쪽은 min heap을 써서 비교

# In[2]:


# 시간 초과
import heapq
import sys

N = int(input())

leftheap = []
rightheap = []
ans = []

for i in range(N):
    num = int(input())
    if(i%2 == 0): # 하나씩 번갈아 가며 넣기 -> 먼저넣는걸 left에 넣음
        heapq.heappush(leftheap, -num)  # max heap 만들고자 - 붙임
    else:
        heapq.heappush(rightheap, num) # 개수 다르면 오른쪽에 넣어서 개수 맞춰주기    
    if(len(leftheap) != len(rightheap)): # 개수 서로 다르면 홀수
        print(-leftheap[0])
    else: # 개수가 같으면 짝수
        temp1 = leftheap[0]
        temp2 = rightheap[0]
        if(-temp1 < temp2):
            print(-temp1)
        else:
            print(temp2)


# In[10]:


# input 쓰면 시간 초과뜸 -> sys
import heapq
import sys

N = int(sys.stdin.readline())

leftheap = []
rightheap = []

for i in range(N):
    num = int(input())
    if i%2 == 0: # 하나씩 번갈아 가며 넣기 -> 먼저넣는걸 left에 넣음
        heapq.heappush(leftheap, -num)  # max heap 만들고자 - 붙임
    else:
        heapq.heappush(rightheap, num) 
    if leftheap and rightheap and -leftheap[0] > rightheap[0]: # 왼쪽 힙이 무조건 더 작은 수 오게끔 만들기
        heapq.heappush(leftheap,-heapq.heappop(rightheap)) # 오른쪽에서 작은거 빼서 왼쪽에 넣고
        heapq.heappush(rightheap,-heapq.heappop(leftheap)) # 왼쪽거는 오른쪽에 넣기
    print(-leftheap[0])

