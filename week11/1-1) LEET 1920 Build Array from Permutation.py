#!/usr/bin/env python
# coding: utf-8

# #### ans[i] = nums[nums[i]] 만족하는 ans 배열 만들기

# In[ ]:


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for i in range(len(nums)):
            a = nums[i]
            b= nums[a]
            ans.append(b)
        return ans       

