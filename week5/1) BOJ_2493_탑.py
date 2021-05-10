#!/usr/bin/env python
# coding: utf-8

# In[18]:


stack = []
result = []
num = int(input())
tower = list(map(int, input().split()))

for i in range(len(tower)):
    if(len(stack)>0):
        for j in range(len(stack)):
            if(stack[-1][0] < tower[i]):
                stack.pop() # 어쨌든 더 최근거 보다 짧은 거는 의미 없어서 다 빼
                if(len(stack) == 0): # 내 앞 다 확인했는데 없으면 내가 제일 긴거
                    stack.append([tower[i],i+1])
                    result.append(0)
            else: # 내 앞이 길어서 쏠 수 있어
                result.append(stack[-1][1])
                stack.append([tower[i],i+1])
                break
            
    else: # 초기 (스택 빈 경우)
        stack.append([tower[i],i+1]) # 탑 길이, 탑 번호
        result.append(0)
for i in result:
    print(i)

