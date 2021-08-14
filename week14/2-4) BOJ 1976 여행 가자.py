#!/usr/bin/env python
# coding: utf-8

# #### 여행 가자
# 
# 경유 가능, 양방향
# 
# i -> j 연결 정보 (1 = 연결됨, 0 = 연결 안됨)
# 
# 입력: 도시의 수, 여행계획에 속한 도시의 수, 연결 정보, 여행 계획
# 
# 출력: 도시 여행 가능 여부

# In[4]:


n = int(input()) # 도시 수
m = int(input()) # 여행계획에 속한 도시 수

graph = [list(map(int, input().split())) for _ in range(n)] # 연결 정보

# 플로이드-워셜
for i in range(n):
    for j in range(n):
        if graph[i][j] == 0 and i != j:  # 길 없는 경우
            graph[i][j] = int(1e9)
for k in range(n):
    for i in range(n):
        for j in range(n):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j]) # k 거치는 것이 더 빠른가?

            
# 여행 가능 여부
plan = list(map(int, input().split())) # 여행 계획
flag = True 
temp = plan[0] - 1 # 인덱스로 맞추기 (-1)
for i in range(1, m): # m개의 도시 여행 계획
    if graph[temp][plan[i] - 1] >= int(1e9):  # 길이 없는 경우 
        flag = False
        break
    else: # 길 있으면 그 다음으로 넘어가서 가능한지 또 확인
        temp = plan[i] - 1

if flag:
    print("YES")
else:
    print("NO")

