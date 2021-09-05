#!/usr/bin/env python
# coding: utf-8

# #### 도시 분할 계획
# 
# 마을 두개로 분할 => 마을 안 집들 사이에는 반드시 경로 존재
# 
# 임의의 두 집 사이 반드시 경로 존재 + 길의 유지비 합 최소
# 
# => 즉, 모든 집 이어지는 경로 찾은 후 거기서 가장 간선 길이가 긴 것을 끊으면 마을이 분할되면서 최소 유지비를 구할 수 있음
# 
# 
# 입력: 1줄(집 개수, 길 개수), 2줄(길의 정보) A B C (A번과 B번 집을 연결하는 길 유지비 C)
#     
# 출력: 없애고 남은 길 유지비 합

# In[6]:


import heapq
import sys

input = sys.stdin.readline

N,M = map(int,input().split())
visited = [False] * (N+1)
graph = [[] for i in range(N+1)]

for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
def prim(start):
    maxcost = 0
    q = []
    visited[start] = True
    cnt = 1 # 간선 개수
    cost = 0 # 비용
    
    for a in graph[start]: # 인접 간선 확인 
        heapq.heappush(q,a)
        
    while q:
        c, v = heapq.heappop(q) # 최소 비용 드는 간선 뽑기
        if not visited[v]:
            visited[v] = True
            cost += c
            cnt += 1
            if c > maxcost: # 최대 비용 찾기 위함
                maxcost = c
            for a in graph[v]: # 그 다음 인접 정보 보기 
                heapq.heappush(q,a)

            if cnt == N: # 최대 비용인 곳 제외 모든 곳 방문했으면 비용 return
                return cost - maxcost
        
print(prim(1))   

