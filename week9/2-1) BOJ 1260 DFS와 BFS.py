#!/usr/bin/env python
# coding: utf-8

# ### 1260 DFS와 BFS
# 
# 
# #### 입력: 정점 개수, 간선 개수, 탐색 시작할 정점 번호
# #### 다음 M개의 줄에는 간선이 연결하는 두 정점 번호가 주어짐
# 
# #### 출력: 첫째 줄에 DFS 수행 결과, 둘째 줄에 BFS 수행결과
# 
# 
# 
# <두 정점 번호가 주어져서 이를 행렬로 표현>

# In[41]:


from collections import deque

N,M,V = map(int,input().split()) 
visited = [False] * (N+1)
queue = []
graph = [[0]*(N+1) for i in range(N+1)]

# graph에 입력 값 넣기
for i in range(M):
    a,b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

def DFS(graph,v,visited):
    visited[v] = True
    print(v, end = ' ')
    for i in range(1,N+1):
        if graph[v][i] == 1 and visited[i] is False: # visit 안했는데 해야할 곳
            DFS(graph,i,visited)
            
def BFS(graph,start,visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in range(1,N+1):
            if graph[v][i] == 1 and visited[i] is False: # visit 안했는데 해야할 곳
                queue.append(i)
                visited[i] = True

DFS(graph,V,visited)
print()
visited = [False] * (N+1)
BFS(graph,V,visited)  

