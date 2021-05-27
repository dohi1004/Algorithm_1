#!/usr/bin/env python
# coding: utf-8

# #### 오큰수
# Ai의 오큰수 = 오른쪽에 있으면서 Ai보다 큰 수 중 가장 왼쪽의 수
# 
# 없는 경우 -1
# 
# -> 구현 = 스택 사용, 들어올 수가 스택안의 수보다 크면 그 전에 들어온 수 모두 그 수로 업데이트

# In[13]:


n = int(input())
num = list(map(int, input().split()))
stack = []
result = [-1] * n

for i in range(n):
    while stack and (stack[-1][0] < num[i]) : # 스택 차있고, 스택안의 수가 만난 수보다 작으면
        temp, index = stack.pop()
        result[index] = num[i] # 만난 큰 숫자로 result를 모두 업데이트
    stack.append([num[i],i]) # 스택안의 수가 만난 수보다 크면 스택 업데이트(값, 인덱스)

for i in result:
    print(i)

