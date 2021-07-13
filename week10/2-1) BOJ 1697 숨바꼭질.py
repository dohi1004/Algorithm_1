#!/usr/bin/env python
# coding: utf-8

# #### 수빈이가 동생한테 가는 최단 시간 찾기
# #### 위치 x 일때 행동 -> +1, -1, *2 
# 
# 
# 입력: 수빈이가 있는 위치, 동생이 있는 위치
#     
# 출력: 최단 시간

# In[25]:


from collections import deque

n,m = map(int, input().split()) # 수빈이의 위치, 동생의 위치
Max = 100000
time = [0] * (Max + 1)

def bfs():
    queue = deque()
    queue.append(n)
    while queue:
        x = queue.popleft()
        if(x == m):
            print(time[x])
            break
        for nx in (x-1,x+1,x*2):
            if 0 <= nx <= Max and not time[nx]: # nx가 다시 같은게 되면 의미 없음(이미 거쳐감)
                time[nx] = time[x] + 1
                queue.append(nx)
bfs()                

