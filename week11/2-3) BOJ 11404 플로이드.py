#!/usr/bin/env python
# coding: utf-8

# #### 플로이드
# n개의 도시 중 한 도시에서 출발하여 다른 도시에 도착하는 m개의 버스가 존재하며, 각 비용은 다름
# 
# 모든 도시 쌍에 대해 A->B로 가는 비용의 최솟값을 구하기
# 
# <갈 수 없는 경우, 0 출력>
# 
# 
# 입력: 노드 개수, 간선 개수, 간선 정보
# 
# 출력: i->j로 가는 비용의 최솟값 출력

# In[1]:


import sys 
INF = int(1e9)
input = sys.stdin.readline
n = int(input()) # 노드 개수(도시)
m = int(input()) # 간선 개수(버스)
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m): # 간선 정보
    a,b,c = map(int, input().split())
    if graph[a][b] > c:
        graph[a][b] = c   
    
for k in range(1,n+1): # 플로이드 워셜
    for a in range(1,n+1):
        for b in range(1,n+1):
            if a == b: # 자기 자신 -> 자기 자신으로 가는 비용은 0으로 초기화
                graph[a][b] = 0 
                continue
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b]) # k를 거쳐 가는 것이 더 빠른가?
            
for a in range(1,n+1):
    for b in range(1,n+1):
        if graph[a][b] == INF: # 도달할 수 없는 경우
            print(0, end = " ")
        else:
            print(graph[a][b], end = " ")
    print()
            

