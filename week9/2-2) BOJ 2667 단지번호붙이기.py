#!/usr/bin/env python
# coding: utf-8

# #### 입력: 지도의 크기 N (정사각형), 다음 N줄에 각 N개의 자료
# #### 출력: 1. 총 단지 수, 2. 각 단지내 집의 수 (오름차순 정렬)
# 
# #### 출력 뭐 해야하는지 잘 보기! 

# In[17]:


n = int(input())

graph = [list(map(int,input())) for _ in range(n)]

def dfs(x,y):
    global count
    # 주어진 범위 벗어남 -> 종료
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False    
    # 현재 노드를 아직 방문 안했으면
    if graph[x][y] == 1:
        graph[x][y] = 0 # 방문 표시
        count += 1
        # 상, 하, 좌, 우 재귀 호출
        dfs(x-1,y)
        dfs(x,y-1)
        dfs(x+1,y)
        dfs(x,y+1)
        return True    
    return False ## 0인 경우 (단지 아님)

nums = 0 # 단지 개수
count = 0 # 각 단지내 짐의 수
resultlist = []
for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            resultlist.append(count)
            count = 0
            nums += 1
print(nums)
resultlist = sorted(resultlist) # 오름차순 정렬
for i in resultlist:
    print(i)

