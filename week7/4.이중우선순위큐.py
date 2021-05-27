#!/usr/bin/env python
# coding: utf-8

# #### 이중 우선순위 큐
# 
# I (숫자) => 숫자 넣기
# 
# D 1 => 최대값 삭제
# 
# D -1 => 최소값 삭제
# 
# 빈 경우 => [0,0] 
# 
# else: [최대값, 최소값]

# In[36]:


import heapq
def solution(operations):
    minheap = []
    maxheap = []
    for i in operations:
        if(i[0] == 'I'): # 값 넣기
                heapq.heappush(minheap, int(i[2:])) 
                heapq.heappush(maxheap, -int(i[2:]))

        else:
            if(i[2] == '1'): # 최대값 삭제
                if(minheap and maxheap): # 빈 상태가 아닌경우
                    temp = -heapq.heappop(maxheap) # 최대힙에서 값 빼고
                    minheap.remove(temp) #이걸 minheap에서도 삭제
            else: # 최솟값 삭제
                if(minheap and maxheap): # 빈 상태가 아닌경우 (동일한 프로세스)
                    temp = heapq.heappop(minheap)
                    maxheap.remove(-temp)
    if(maxheap and minheap):
        ans = []
        ans.append(-heapq.heappop(maxheap))
        ans.append(heapq.heappop(minheap))
        answer = ans
    else:
        answer = [0,0]
    return answer

