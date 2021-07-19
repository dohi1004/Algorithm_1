#!/usr/bin/env python
# coding: utf-8

# #### 키 순서 (학생들의 키 비교 결과가 주어졌을 때, 자신의 키가 몇 번째인지 알 수 있는 학생의 수 구하기)
# 
# a 학생이 b 학생보다 키가 작으면 a에서 b로 화살표 그림
# 
# 입력: 1줄(학생 수(노드), 두 학생 키 비교 횟수(간선)) 2줄~(두 학생 키 비교 결과(a,b) => a가 b보다 작음을 의미)
#     
# 출력: 자신의 키가 몇 번째인지 알 수 있는 학생의 수 

# In[8]:


import sys
input = sys.stdin.readline
n,m = map(int, input().split())
count = 0
graph = [[0] * (n+1) for _ in range(n+1)]

for i in range(m): # 간선 (a -> b) 작은거에서 큰거로 화살표 방향!
    a, b = map(int, input().split())
    graph[a][b] = 1
     
for k in range(1,n+1): # 플로이드 워셜
    for a in range(1,n+1):
        for b in range(1,n+1):
            if graph[a][k] == 1 and graph[k][b] == 1: # 거쳐서 갈 수 있는 경우 1로 업데이트
                graph[a][b] = 1

count = 0
for a in range(1,n+1): # 몇 번째 순서인지 알기 위해서는 다른 노드 모두 1 돼야함(즉, 자기 제외 n-1 정점이 자신을 가르켜야함)
    temp = 0
    for b in range(1,n+1):
        temp += graph[a][b] + graph[b][a] # 즉, 1번이 나머지 가르키는 횟수 + 나머지가 1번 가르키는 횟수가 총 n-1되어야함!
        
    if temp == n-1:
        count += 1
    
    
print(count)


# In[ ]:




