#!/usr/bin/env python
# coding: utf-8

# #### 전화번호 목록
# 
# 일관성 -> 입력 도중 다른 전화번호랑 겹치면 없는 것 (ex - 911, 9113)
# 
# 입력: 테스트 케이스 수 , 각 테스트 케이스 수의 전화번호 수, 전화번호
# 
# 출력: 일관성 o = YES, 일관성 x = NO

# In[2]:


import sys
#input = sys.stdin.readline
n = int(input()) # 테스트 케이스 수
answer = []
numbers = []
check = True
for i in range(n):
    m = int(input()) # 전화번호 수
    for j in range(m):
        h = input().strip()
        numbers.append(h)
    numbers.sort()
    for i in range(len(numbers)-1): # 나랑 뒤에거 비교하니까 -1(마지막은 굳이 할필요 없음)
        if numbers[i] in numbers[i+1][:len(numbers[i])]:
            answer.append('NO')
            check = False
            break
    if check: # 만약 No가 아니라면
        answer.append('YES')
    numbers = [] # 초기화, 그 다음 테스트 케이스 시작
    check = True       
for i in answer:
    print(i)

