#!/usr/bin/env python
# coding: utf-8

# #### 방향 그래프 주어지면, 주어진 시작점에서 다른 모든 정점으로의 최단 경로 구하기
# 
# 입력: 정점 개수, 간선 개수, 시작점
#     
# 출력: 시작점 0 기준으로 모든 정점으로의 최단 경로

# In[13]:


import sys
import heapq 
input = sys.stdin.readline

INF = int(1e9)
V,E = map(int, input().split()) # 정점 개수, 간선 개수
K = int(input()) # 시작 정점 번호 
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E): 
    a,b,c = map(int, input().split())
    graph[a].append((b,c)) # a -> b 가는데 드는 비용 c
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0,start)) # 시작노드로 가는 최단 경로 = 0
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist: # 이미 처리된 적 있는 노드라면 무시
            continue
        for i in graph[now]: # 현재 노드와 연결된 다른 인접한 노드들 확인
            cost = dist + i[1]
            if cost < distance[i[0]]: # 다른 노드로 가는게 더 빠른 경우
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
dijkstra(K)

for i in range(1,V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])

