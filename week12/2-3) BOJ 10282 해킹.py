#!/usr/bin/env python
# coding: utf-8

# #### 해킹
# 
# 컴퓨터 한 대가 해킹 당하면 의존성이 있는 다른 컴퓨터들에 전염됨 (a가 b에 의존시, b 감염되면 특정 시간 이후 a도 감염)
# 
# 해킹 당한 컴퓨터 포함해서 총 몇대의 컴퓨터 감염 + 걸리는 시간
# 
# 입력: 1줄(테스트 케이스 수), (컴퓨터 개수, 의존성 개수, 해킹당한 컴퓨터 번호) / (의존성)
# 
# 출력: 각 테스트 케이스마다 한 줄에 총 감염된 컴퓨터 수 + 마지막 컴퓨터 감염되는데 걸린 시간 

# In[8]:


import heapq
import sys
input = sys.stdin.readline
tn = int(input()) # 테스트 케이스 수 
INF = int(1e9)
       
for _ in range(tn):
    # 매 테스트 케이스, 값 초기화
    count = 0
    time = 0
    time_list = []
    graph = [[] for _ in range(n+1)]
    distance = [INF] * (n+1)
    
    n,d,hacking = map(int, input().split()) # 노드 수 (컴퓨터 개수), 간선 수 (의존성 개수), 해킹 당한 컴퓨터 번호 
    for i in range(d): # 간선 정보
        a,b,c = map(int, input().split())
        graph[b].append((a,c)) # a가 b에 의존, b 감염시 a는 c초후 감염 
    
    # 다익스트라 
    q = []
    heapq.heappush(q, (0,hacking))
    distance[hacking] = 0 
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]: 
            cost = dist + i[1]
            if  cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost,i[0]))
    
    # 결과 출력
    for i in distance:
        if i != INF: 
            count += 1 # 컴퓨터 개수 증가
            time_list.append(i) 
    time = max(time_list) # 가장 오래 걸린 시간 찾기
    print(count, time, end = ' ')

