#!/usr/bin/env python
# coding: utf-8

# #### 최소값과 최대값 구하기
# 
# 쌍이 주어졌을 때 그 구간 안에서 최대값과 최소값 구하기
# 
# 입력: 수의 개수(n), 쌍의 개수(m), n줄(수), m줄(a,b 쌍)
#     
# 출력: m개의 줄에 순서대로 a,b에 대한 답을 최솟값, 최대값 순서로 출력

# #### 세그먼트 트리
# https://m.blog.naver.com/ndb796/221282210534

# In[12]:


import sys
input = sys.stdin.readline

n,m = map(int, input().split())

mintree = [0] * (n*4)
maxtree = [0] * (n*4)
array = [0] * n

# 최소 트리 초기화
def mininit(start,end,index): 
    if start == end: # 리프
        mintree[index] = array[start]
        return mintree[index]
    
    mid = (start+end) // 2
    # 재귀적으로 두 부분으로 나눈 뒤 그 최솟값을 자기 자신으로 함
    mintree[index] = min(mininit(start,mid,index*2), mininit(mid+1,end,index*2+1))
    return mintree[index]

# 구간 주어질 때 최솟값 반환
def minquery(start,end,index,left,right):
    if left > end or right < start: # 구간 벗어난 경우
        return int(1e9)
    if left <= start and end <= right: # 구간 내
        return mintree[index] # 해당 트리 값 반환
    # 트리 타고 밑으로 내려가기
    mid = (start+end) // 2 
    return min(minquery(start,mid,index*2,left,right), minquery(mid+1,end,index*2+1,left,right))

# 최대 트리 초기화
def maxinit(start,end,index):
    if start == end: # 리프
        maxtree[index] = array[start]
        return maxtree[index]

    mid = (start+end) // 2
    # 재귀적으로 두 부분으로 나눈 뒤 그 최대값을 자기 자신으로 함
    maxtree[index] = max(maxinit(start,mid,index*2), maxinit(mid+1,end,index*2+1))
    return maxtree[index]

# 구간 주어질 때 최대값 반환
def maxquery(start,end,index,left,right):
    if left > end or right < start: # 구간 벗어난 경우
        return 0
    if left <= start and end <= right: # 구간 내
        return maxtree[index]
    # 트리 타고 밑으로 내려가기
    mid = (start+end) // 2
    return max(maxquery(start,mid,index*2,left,right), maxquery(mid+1,end,index*2+1,left,right))


for i in range(n):
    a = int(input())
    array[i] = a

# 최소, 최대 트리 만들기
mininit(0,n-1,1)
maxinit(0,n-1,1)

for i in range(m): # 주어진 구간 쌍 받기
    a,b = map(int,input().split())
    print(minquery(0,n-1,1,a-1,b-1),end=' ') 
    print(maxquery(0,n-1,1,a-1,b-1)) 

