#!/usr/bin/env python
# coding: utf-8

# #### 경로 찾기
# 
# 입력 : 정점의 개수, 인접 행렬 (0: 간선 없음, 1: 간선 존재)
# 
# 출력 : i에서 j로 가는 경로 있으면 1로해서 인접행렬 형식으로 출력

# In[9]:


N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]

for k in range(N):
    for a in range(N):
        for b in range(N):
            if graph[a][k] and graph[k][b]: # a -> k, k -> b이면, a -> b
                graph[a][b] = 1

for line in graph:
    print(*line) # unpacking

