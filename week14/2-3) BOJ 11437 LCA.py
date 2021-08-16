#!/usr/bin/env python
# coding: utf-8

# #### 최소 공통 조상 구하기
# 
# 루트 = 1
# 
# 두 노드 쌍이 주어졌을 때 가장 가까운 공통 조상 몇 번인지 출력
# 
# 입력: 노드의 개수, 트리 상 연결된 두 정점, 가장 가까운 공통 조상 알고싶은 쌍의 개수, 정점 쌍
#     
# 출력: m개의 줄에 입력받은 두 정점의 가장 가까운 공통 조상

# In[ ]:


import sys
sys.setrecursionlimit(int(1e5))

n = int(input())

parent = [0] * (n+1) # 부모 노드 정보
d = [0] * (n+1) # 각 노드까지 깊이
c = [0] * (n+1) # 깊이 계산 여부
graph = [[] for _ in range(n+1)]

for _ in range(n-1): # 그래프 정보 
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
    
# 루트 노드부터 시작해 깊이를 구하는 함수
def dfs(x,depth):
    c[x] = True # 방문 표시
    d[x] = depth # 매 노드마다 깊이 기록
    for y in graph[x]: # 인접 노드 확인
        if c[y]: # 이미 깊이 구한 경우 넘기기
            continue
        # 인접한 노드의 부모를 현재 노드로 기록
        parent[y] = x
        # 해당 노드 기준 depth 1 증가시키고 다시 dfs
        dfs(y,depth+1)

# a와 b의 최소 공통 조상 찾기
def lca(a,b):
    while d[a] != d[b]: # 깊이 같을때까지
        if d[a] > d[b]: # a 깊이가 더 깊으면
            a = parent[a] # a의 부모노드로
        else: # 반대는
            b = parent[b] # b의 부모노드로
            
    # 깊이 같아졌으면 공통 조상 찾기           
    while a != b: # 같지 않은 경우 동시에 부모 노드로 
        a = parent[a]
        b = parent[b]
        
    # 공통 조상 리턴
    return a

dfs(1,0) # 루트 노드에서 시작, depth = 0

m = int(input())

for i in range(m):
    a,b = map(int,input().split())
    print(lca(a,b))

