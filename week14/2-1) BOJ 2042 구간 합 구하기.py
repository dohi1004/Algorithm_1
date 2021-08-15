#!/usr/bin/env python
# coding: utf-8

# #### 구간 합 구하기
# 
# 입력: 1줄(수의개수, 변경 횟수, 구간 합 구하는 횟수), 2\~N+1줄(N개의 수), N+2~N+M+K+1줄(a,b,c) 
#     
# a = 1, b번째 수를 c로 바꾸기
# 
# a = 2, b번째 수부터 c번째 수까지의 합을 구하여 출력 

# #### 참고
# 바이너리 인덱스 트리(펜윅 트리)
# 
# https://www.acmicpc.net/blog/view/21

# In[1]:


import sys
input = sys.stdin.readline

# 수 개수, 변경 횟수, 구간 합 구하는 횟수
n, m, k = map(int, input().split())

arr = [0] * (n+1)
tree = [0] * (n+1)

# i번째 수까지 누적 합 구하기(0이 아닌 마지막 비트만큼 빼면서 구간들의 합 계산)
def prefix_sum(i):
    result = 0
    while i > 0: # 트리 끝까지 볼때까지
        result += tree[i]
        i -= (i&-i) # ex) 1 2 3 4, 3까지 합 구할시 3 + (1~2) 해야함. // 3먼저 본다음 0 아닌 비트(1) 빼서 인덱스 2 확인함
    return result

# 값 변경하기
def update(i,dif):
    while i<=n: # 자기를 포함하는 것 모두 볼때까지
        tree[i] += dif # tree에서 0이 아닌 마지막 비트만큼 더하며 이동
        i += (i&-i) # ex) 1 2 3 4 에서 3 변경시, 3, 1~4를 변경해야함 // 그 다음 3+1번째 배열 보면 1~4를 변경하게 되어있음

# 구간 합 구하기
def interval_sum(start,end):
    return prefix_sum(end) - prefix_sum(start-1)

for i in range(1,n+1): # arr 인덱스 1부터 하기 위함
    x = int(input()) # 수
    arr[i] = x 
    update(i,x) # tree update // 트리의 경우 1 = 1, 2 = 1~2, 3 = 3, 4 = 1~4 이런식으로 담고 있음
    # 1->2->4 이 순서로 update // 2는 2->4 // 3 -> 4 // 4 -> 4 // 5 -> 5
    
for i in range(m+k): 
    a,b,c = map(int,input().split())
    if a == 1:
        update(b,c-arr[b]) # 바뀐 크기만큼 적용
        arr[b] = c
    else: # 구간합 연산
        print(interval_sum(b,c))

