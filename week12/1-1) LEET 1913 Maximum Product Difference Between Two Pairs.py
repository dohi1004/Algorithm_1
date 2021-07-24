#!/usr/bin/env python
# coding: utf-8

# #### 리스트에서 4원소를 뽑아서, a - b 와 c - d 를 곱한 값이 최대인 것 구하기

# In[3]:


class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        return (nums[-1] * nums[-2]) - (nums[0] * nums[1])

