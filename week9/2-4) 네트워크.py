#!/usr/bin/env python
# coding: utf-8

# #### 입력: 컴퓨터 개수(n), 연결에 대한 정보(computers)
# #### 출력: 네트워크 개수 (연결되어 있는 거는 한 네트워크로 봄)

# In[11]:


def solution(n, computers):
    def dfs(graph,v,visited):
        visited[v] = True # 방문 표시
        for i in range(n):
            if graph[v][i] == 1 and visited[i] is False: # 방문해야하는데 아직 안한거
                dfs(graph,i,visited)
            
    visited = [False] * n # 방문 초기화
    answer = 0
    for i in range(n):
        if visited[i] is False: # 방문 아직 안했으면
            dfs(computers,i,visited) # 방문 -> 그거랑 연결한거 다 방문하면
            answer += 1 # 네트워크 개수 카운트
    return answer

