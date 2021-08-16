#!/usr/bin/env python
# coding: utf-8

# #### 중량 제한
# 
# 각 다리마다 중량 제한이 있음 => 중량제한을 초과하는 양의 물품을 지나면 다리가 무너짐
# 
# 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최댓값 구하기
# 
# 서로 같은 두 섬 사이 여러 개의 다리가 있을 수 있고, 모든 다리는 양방향
# 
# 입력: 섬 개수, 다리 정보 개수(m), a,b,c(m개의 줄), 공장 위치한 섬 번호(마지막 줄)
#     
#     a번 섬과 b번 섬 사이 중량제한이 c인 다리 존재
#     
# 출력: 한 번의 이동에서 옮길 수 있는 물품들의 중량의 최대값

# In[2]:


import sys
from collections import deque

input = sys.stdin.readline
n,m = map(int,input().split())
graph = [[] for _ in range(n+1)]


# 그래프 생성
for _ in range(m):
    a,b,c = map(int, input().split()) #a,b = 섬, c = 중량제한
    graph[a].append((b,c))
    graph[b].append((a,c))
    
start, end = map(int,input().split()) # 공장 위치한 섬 번호

minnum, maxnum = 1, 1000000000 # 중량제한 최소, 최대

# 갈 수 있는지 여부 확인
def bfs(target):
    visited = [0 for _ in range(n+1)]
    visited[start] = 1
    queue = deque([start])
    while queue:
        x = queue.popleft()
        if x == end: # 도달 가능한 경우 true 리턴
            return True
        for v,w in graph[x]: 
            # 방문 x & 무게 제한 걸리지 않을 경우
            if not visited[v] and w >= target:
                visited[v] = 1
                queue.append(v)
    return False
        
        
# 이분 탐색 => 최대 중량 찾기
result = minnum
while minnum <= maxnum:
    mid = (minnum + maxnum) // 2
    # 해당 무게로 start->end 도달 가능하면 값 저장, 최대값 구하고자 min 올려서 반복
    if bfs(mid):
        result = mid
        minnum = mid + 1
    else:
        maxnum = mid - 1 # 도달 불가능하면 max 값 낮추기
print(result)


# In[ ]:




