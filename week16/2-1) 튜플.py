#!/usr/bin/env python
# coding: utf-8

# #### 특정 튜플을 표현하는 집합이 담긴 문자열 s가 표현하는 튜플 반환하기
# 
# * 튜플의 성질
# 1. 중복된 원소가 있을 수 있습니다. ex : (2, 3, 1, 2)
# 2. 원소에 정해진 순서가 있으며, 원소의 순서가 다르면 서로 다른 튜플입니다. ex : (1, 2, 3) ≠ (1, 3, 2)
# 3. 튜플의 원소 개수는 유한합니다.
# 
# 원소의 개수가 n개이고, 중복되는 원소가 없는 튜플 (a1, a2, a3, ..., an)이 주어질 때(단, a1, a2, ..., an은 자연수)
# 다음과 같이 집합 기호 '{', '}'를 이용해 표현할 수 있음
# 
# {{a1}, {a1, a2}, {a1, a2, a3}, {a1, a2, a3, a4}, ... {a1, a2, a3, a4, ..., an}}
# 
# (이때, 집합은 원소간 순서 변경될 수 있음)
# 
# 입력: 문자열 s
#     
# 출력: s가 표현하는 튜플 리스트에 담아 반환

# In[25]:


def solution(s):
    answer = []
    s = s[2:-2] # {{,}} 제거
    s = s.split("},{") # 중괄호 기준 split
    s.sort(key = len) # 길이 기준 정렬
    for i in s:
        sp1 = i.split(',') # 콤마 기준 split
        for j in sp1: 
            if int(j) not in answer: # 만약 해당 숫자가 answer에 없으면
                answer.append(int(j)) # 추가

    return answer

