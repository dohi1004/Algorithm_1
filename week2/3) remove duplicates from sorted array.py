#!/usr/bin/env python
# coding: utf-8

# In[1]:


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        if(len(nums) == 0):
            return 0
        past = nums[0]
        init = nums[0]

        for i,v in enumerate(nums):   
            if(v == past):
                nums[i] = 'dup'
            else:
                past = v
        nums[0] = init
        num = len(nums)
        for i in range(num):
            if('dup' in nums):
                nums.remove('dup')
        return(len(nums))
nums = []
answer = Solution()
leng = answer.removeDuplicates(nums)
print(nums)
for i in range(0,leng):
    print(nums[i])

