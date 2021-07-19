#!/usr/bin/env python
# coding: utf-8

# #### X번 마을에서 파티를 벌이는데, 오고 가는 길이 가장 긴 학생의 거리 반환하기
# 
# N개의 마을에 한 명씩 학생이 살고 있음
# 
# M개의 단방향 도로 존재(즉, 오고 갈때의 길이 달라질 수 있음)
# 
# 입력: 1줄(노드 개수, 간선 개수, 파티장소(시작점)) 2줄~(도로 시작점, 끝점, 걸리는 시간)
#     
# 출력: 오고 가는데 가장 오래 걸린 학생의 시간
# 

# In[9]:


import heapq
import sys

# input = sys.stdin.readline
INF = int(1e9)

n, m, start = map(int, input().split()) # 노드 개수 , 간선 개수, 시작 노드
graph = [[] for i in range(n+1)] # 연결된 노드 정보 담는 리스트
rev_graph = [[] for i in range(n+1)] # 역방향 그래프
distance = [INF] * (n+1) # 최단 거리 테이블 모두 무한으로 초기화
rev_distance = [INF] * (n+1)

for _ in range(m): # 간선 정보
    x, y, z = map(int, input().split())
    graph[x].append((y,z)) # x번 노드에서 y 노드로 가는 비용이 z
    rev_graph[y].append((x,z)) # y번 노드에서 x 노드로 가는 비용이 z
    
def dijkstra(start,graph, distance):
    q = []
    heapq.heappush(q, (0,start))
    distance[start] = 0
    
    while q:
        dist, now = heapq.heappop(q) # 최단거리 가장 짧은 것 뽑기
        if distance[now] < dist: 
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start, graph, distance) # 정방향 (특정지점에서 돌아감)
dijkstra(start, rev_graph, rev_distance) # 역방향 (출발해서 특정 지점 도착)
total_distance = []

for i in range(len(distance)):
    if distance[i] != INF and rev_distance[i] != INF: # 둘 다 무한이 아닌 경우
        total_distance.append(distance[i] + rev_distance[i]) # 총 거리에 둘이 더해서 넣기
    
print(max(total_distance)) # 최대 시간 걸린 것 출력

