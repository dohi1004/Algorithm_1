#!/usr/bin/env python
# coding: utf-8

# #### 1번에서 N번 정점 갈 때 임의의 두 정점 반드시 거치는 최단 경로 구하기
# 
# 방향성 없는 그래프 (양방향)
# 
# 입력: 1줄(정점 개수(N), 간선 개수) 2줄~(a->b까지 거리 c), 마지막줄(반드시 거쳐야 하는 두 정점 번호)
# 
# 출력: 1번 정점에서 특정한 두 정점 번호 반드시 거쳐서 N에 도달하는 최단 경로

# In[7]:


import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)
start = 1 # 시작 노드 = 1번 정점
n, m = map(int, input().split()) # 노드 개수 , 간선 개수
graph = [[] for i in range(n+1)] # 연결된 노드 정보 담는 리스트


for _ in range(m): # 간선 정보
    x, y, z = map(int, input().split())
    graph[x].append((y,z)) # x번 노드에서 y 노드로 가는 비용이 z
    graph[y].append((x,z)) # y번 노드에서 x 노드로 가는 비용이 z (양방향이므로)

def dijkstra(start):
    distance = [INF] * (n+1) # 최단 거리 테이블 모두 무한으로 초기화
    distance[start] = 0
    q = []
    heapq.heappush(q, (0,start))
    while q:
        dist, now = heapq.heappop(q) # 최단거리 가장 짧은 것 뽑기
        if distance[now] < dist: 
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
    return distance
                
n1, n2 = map(int, input().split()) # 반드시 거쳐야 하는 노드 2개


first = dijkstra(start)
second = dijkstra(n1)
third = dijkstra(n2)

route1 = first[n1] + second[n2] + third[n] # 길1: 1 -> n1 -> n2 -> N 
route2 = first[n2] + third[n1] + second[n] # 길2: 1 -> n2 -> n1 -> N
final_route = min(route1,route2)

if final_route < INF: # 그런 경로 존재하지 않으면 -1 출력
    print(final_route)
else: print(-1)

