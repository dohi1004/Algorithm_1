#!/usr/bin/env python
# coding: utf-8

# #### 벽을 3개 세운 후 바이러스가 퍼질 수 없는 안전 영역의 최대 크기 구하기
# 
# 입력: 세로 크기, 가로 크기, 지도 모양(0 = 빈칸, 1 = 벽, 2 = 바이러스)
# 
# 출력: 안전 영역의 최대 크기

# In[5]:


import copy
from itertools import combinations
from collections import deque

N,M = map(int,input().split()) # N = 세로, M = 가로
graph = []
virus_list = []
zero_list = [] 
result_list = []

# 그래프, virus_list(2), zero_list 담기(0)
for i in range(N):
    graph.append(list(map(int,input().split())))
for a in range(N):
    for b in range(M):
        if(graph[a][b] == 0):
            zero_list.append((a,b))
        if(graph[a][b] == 2):
            virus_list.append((a,b))

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def spread(x,y,graph): # 바이러스 전파
    queue = deque()
    queue.append((x,y))
    while queue:
        x,y = queue.popleft()
        for i in range(4): # 상하좌우로 전파
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < N and ny >= 0 and ny < M: # 범위 내
                if graph[nx][ny] == 0: # 빈칸이면
                    graph[nx][ny] = 2 # 바이러스로 바꾸고
                    queue.append((nx,ny)) # 큐에 넣기
                
def safety(graph_): # 안전 구역 게산(0인거 개수)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if(graph_[i][j] == 0):
                cnt += 1
    return cnt

# 3개의 벽이 세워질 경우의 수 
walls = combinations(zero_list, 3)

for wall in walls: # 조합에 따라 0 -> 1로 바꾸는 것
    graph_ = copy.deepcopy(graph)
    graph_[wall[0][0]][wall[0][1]] = 1
    graph_[wall[1][0]][wall[1][1]] = 1
    graph_[wall[2][0]][wall[2][1]] = 1
    
    for virus in virus_list: # 1로 바꾼 다음에 그 곳에 바이러스 전파 후 안전 구역 세기
        spread(virus[0],virus[1],graph_)
    result_list.append(safety(graph_))
    
print(max(result_list))

