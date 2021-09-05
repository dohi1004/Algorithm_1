#!/usr/bin/env python
# coding: utf-8

# #### 스패닝 트리: 그래프 모든 노드 서로 연결 + 사이클 존재 x
# 
# #### 프림 알고리즘
# 그리디 알고리즘을 기초로함
# 시작 정점 선택 -> 인접한 간선중 최소 간선으로 연결된 정점 선택 -> 다시 최소..

# #### 최소 스패닝 트리 (모두 연결 + 최소 비용)
# 
# 주어진 그래프의 모든 정점들을 연결하는 부분 그래프 중에서 그 가중치의 합이 최소인 트리 구하기
# 
# 간선 정보 : A B C = A번 정점과 B번 정점이 가중치 C인 간선으로 연결됨
# 
# 입력: 1줄(정점 개수, 간선 개수), 2줄~(간선 정보)
# 
# 출력: 최소 스패닝 트리의 가중치

# In[9]:


import heapq
import sys

input = sys.stdin.readline
V, E = map(int,input().split())

graph = [[] for i in range(V+1)]
visited = [False] * (V+1)

for i in range(E):
    a,b,c = map(int,input().split())
    graph[a].append((c,b))
    graph[b].append((c,a))
    
    
def prim(start):
    q = []
    visited[start] = True # 방문 표시
    dist = 0
    cnt = 1
    
    for a in graph[start]: # 인접 간선 확인
        heapq.heappush(q,a)
    
    while q:
        c, v1 = heapq.heappop(q) # 가중치 가장 작은 간선 
        if not visited[v1]: # 방문 안했으면
            visited[v1] = True # 방문 표시
            cnt += 1 # 간선 개수
            dist += c # 비용 추가
            
            for a in graph[v1]: # 다음 인접 노드 탐색
                heapq.heappush(q,a)
                
            if cnt == V: # 모든 정점 다 방문했으면
                return dist # 최소 거리 return


print(prim(1))

