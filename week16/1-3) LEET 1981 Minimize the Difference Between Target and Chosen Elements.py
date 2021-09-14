#!/usr/bin/env python
# coding: utf-8

# #### 주어진 리스트에서 각 행마다 한 숫자씩 뽑아서 target과 절대값 차를 가장 작게 만들기
# 
# 입력: 리스트, target
#     
# 출력: 절대값 차를 한 이후 최소화된 값 (target - 최소화시키는 값)

# In[ ]:


from itertools import product
class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        min_sum = 0

        for row in mat:
            min_sum += min(row)
        if min_sum >= target: # 최소값만 더했을 때 이미 target보다 크면 그냥 그거 빼서 반환
            return min_sum - target

        nums = {0}
        for row in mat:
            # target - min_sum보다 크면 탐색할 필요 없음
            # x + i - target > target - min_sum 인 경우 제외 => 즉, <= 일때만 합집합에 삽입
            nums = {x + i for x in row for i in nums if x + i <= 2 * target - min_sum} 


        return min(abs(x - target) for x in nums) # 최종 합 구한것들 중 가장 최소 차 반환
        

