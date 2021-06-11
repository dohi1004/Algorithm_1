#!/usr/bin/env python
# coding: utf-8

# ##### 트리
# 트리가 주어졌을 때, 노드 하나를 지우고 남은 트리에서 리프 노드의 개수 구하기
# 
# ##### 주의
# 루트 노드가 지워 졌을 때 (트리 자체가 날라가 -> 0)

# In[10]:


def dfs(x):
    global answer
    if not tree[x]: # 더이상 자식이 없는 경우 (leaf)
        answer += 1
        return

    for v in tree[x]: # 자식 있으니 자식노드 더보기
        dfs(v)

N = int(input()) # 트리
info = list(map(int, input().split()))
tree = [[] for _ in range(N)] # 각 트리에 자식 몇개있는지 넣을거야 인덱스로
delete = int(input()) # 삭제할 숫자

for i in range(N):
    if info[i] == -1: # -1 -> root
        root = i
        continue
    if i == delete: # 삭제해야 하는거면 건너뛰기
        continue
    tree[info[i]].append(i) # 그 외의 경우 tree에 값넣어(index로! 개수가 주어져있으니까)


answer = 0
if root != delete: # root가 삭제되지 않는지 확인
    dfs(root)
print(answer)

