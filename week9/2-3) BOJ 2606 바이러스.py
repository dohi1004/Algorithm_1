#!/usr/bin/env python
# coding: utf-8

# #### 입력: 1. 컴퓨터 개수 2.연결된 컴퓨터 쌍의 개수 3.연결된 컴퓨터 번호 쌍
# #### 출력: 웜 바이러스에 걸리게 되는 컴퓨터 수 (1번 제외) => 서로 연결이 있으면 전파됨

# In[3]:


n = int(input()) # 컴퓨터 개수
m = int(input()) # 연결된 컴퓨터 번호 쌍
V = 1 # 1번과 연결된 것 찾을 것
graph = [[0]*(n+1) for i in range(n+1)]
visited = [False] * (n+1)
for i in range(m):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def dfs(graph,v,visited):
    visited[v] = True
    for i in range(1,n+1):
        if graph[v][i] == 1 and visited[i] is False: #방문해야하는데 방문 안한 거
            dfs(graph,i,visited)
            
dfs(graph,V,visited) # 1 기준 dfs
count = 0
for i in visited: # 방문된거 개수 세기
    if i is True:
        count += 1
        
print(count-1)

