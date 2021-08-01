#!/usr/bin/env python
# coding: utf-8

# #### 최소의 rungs 추가하기
# 
# rungs라는 리스트가 주어지면, 이를 끝까지 타고 갈때 몇 개의 추가 rung이 필요한가?
# 
# 한 번 건널 때는 dist만큼 건널 수 있으며, 다음 rung이 dist보다 먼 경우 중간에 추가 rung을 설치(같은 height는 설치 x)
# 
# 입력: rungs, dist
# 
# 출력: 최소로 추가할 rungs 개수

# In[17]:


class Solution:
    def addRungs(self, rungs: List[int], dist: int) -> int:
        rungs.insert(0,0) # 땅 추가
        length = len(rungs)
        checklist = []
        answer = 0
        for i in range(length-1):
            checklist.append(rungs[i+1] - rungs[i])

        for i in checklist:
            if i > dist: # 만약 거리를 초과한 경우 (설치 필요)
                if dist == 1: 
                    answer += i - 1 # rungs = [3], dist = 1 [1,2]에 설치 // (3-1)개수만큼 필요. 
                else:
                    if i%dist == 0: # 만약 배수인 경우 1 빼기 (ex, rungs = [12], dist = 4 [4,8]에 설치 몫에서 본인 빼기(12))
                        answer += i//dist -1
                        
                    else: # 배수 아닌 경우는 안 빼고 몫 그대로
                        answer += i//dist     
        return answer

