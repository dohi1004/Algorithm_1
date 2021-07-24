#!/usr/bin/env python
# coding: utf-8

# #### 1번 노드에서 가장 멀리 떨어진 노드 수 구하기
# 가장 멀리 떨어진 노드 = 최단 경로로 이동 시 간선 개수가 가장 많은 노드
# 
# 간선은 양방향
# 
# 입력: 노드 개수 n, 간선에 대한 정보
# 
# 출력: 1번 노드로부터 가장 멀리 떨어진 노드 수 

# In[11]:


import heapq
def solution(n, edge): 
    INF = int(1e9)
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)

    for v in edge:
        graph[v[0]].append(( v[1], 1)) # a -> b까지 가는 비용 1(간선 개수로 최단 거리 계산!)
        graph[v[1]].append(( v[0], 1)) # b -> a 도 양방향!
    def dijkstra():
        q = []
        heapq.heappush(q, (0,1)) # 자기 자신과의 거리 = 0 , 1번 노드
        distance[1] = 0

        while q:
            dist, now = heapq.heappop(q)
            if distance[now] < dist:
                continue
            for i in graph[now]:
                cost = dist + i[1]
                if cost < distance[i[0]]:
                    distance[i[0]] = cost
                    heapq.heappush(q, (cost, i[0]))

    dijkstra()
    max_val= max(distance[1:]) # 가장 먼 거리 구하고 
    return distance.count(max_val) # 몇 개 있는지 세기

