#!/usr/bin/env python
# coding: utf-8

# #### 최대 compatibility score 구하기
# 
# n개의 질문이 0,1의 답으로 구성되어 있음
# 
# m 명의 학생과 멘토들이 있으며, 각 학생은 한 멘토씩 지정받음
# 
# 학생과 멘토가 같은 답을 가지면 compatibility score가 올라감 -> 이를 최대로 하도록 하기
# 
# 입력: students, mentors
# 
# 출력: 최대 compatibility score

# In[13]:


class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        
        n, m = len(students), len(students[0]) # n = 총 학생 수, m = 답안 수
        result = []

        def dfs(i, visited, score): 
            
            if i == n: # 모든 경우 다 보면 최종 결과 붙이기
                result.append(score)
                return
            
            # ex)
            # students a,b,c
            # mentors A,B,C 
            # (a,A) => dfs로 {(b,B) , (c,C)} {(b,C), (c,B)} 해서 모든 경우의 수에 대한 score 다 구함
            # (a,B) => 똑같이 모든 경우의 수
            # (a,C) => 똑같이 모든 경우의 수
            
            for mentor in range(n): # 멘토 모두 돌때까지 
                if str(mentor) not in visited: # 한 학생이 한 멘토에 배정되므로
                    curr = sum(a==b for a, b in zip(students[i], mentors[mentor])) # compatibility score 구하기
                    dfs(i+1, visited+str(mentor), score+curr) # 다음 학생, 멘토는 visited에 넣고, 해당 경우에 대한 compatibility score 더하기
            
        dfs(0, '', 0)
        return max(result) # 구한 compatibiltiy score 중 max 리턴

