#!/usr/bin/env python
# coding: utf-8

# #### 네트워크 연결
# 
# 모든 컴퓨터 연결 + 최소 비용
# 
# 입력: 1줄(컴퓨터 수), 2줄(선의 수), 3줄~(간선 정보) A B C (A 컴퓨터와 B 컴퓨터 연결하는데 드는 비용 C)
#     
# 출력: 모든 컴퓨터 연결하는데 드는 최소 비용

# In[1]:


import heapq
import sys

input = sys.stdin.readline

N = int(input())
M = int(input())

visited = [False] * (N+1)
graph = [[] for i in range(N+1)]

for i in range(M):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
def prim(start):
    q = []
    cnt = 1
    cost = 0
    visited[start] = True 
    
    for a in graph[start]: # 인접한 간선 확인
        heapq.heappush(q,a)
        
    while q:
        c, v = heapq.heappop(q) # 최소 거리 간선 
        
        if not visited[v]: # 방문 안했으면
            visited[v] = True # 방문 표시
            cost += c # 비용 더하기
            cnt += 1 # 간선 개수 추가
            
            for a in graph[v]: # 인접 정보 확인
                heapq.heappush(q,a)

            if cnt == N: # 모든 노드 방문시 끝
                return cost

print(prim(1))

