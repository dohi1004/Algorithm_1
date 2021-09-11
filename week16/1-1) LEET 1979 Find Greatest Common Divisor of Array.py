#!/usr/bin/env python
# coding: utf-8

# #### 주어진 리스트에서 최대 공약수 구하기
# 
# 입력: nums 리스트
# 
# 출력: 최솟값과 최대값의 최대 공약수 

# In[ ]:


class Solution:
    def findGCD(self, nums: List[int]) -> int:
        minnum = min(nums)
        maxnum = max(nums)
        for i in range(minnum,0,-1):
            if minnum % i == 0 and maxnum % i == 0:
                return i

