#!/usr/bin/env python
# coding: utf-8

# sol1

# In[2]:


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


# sol2

# In[6]:


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """    
        nums[:] = sorted(set(nums))
        return(len(nums))
    
nums = [1,2,3,3]
answer = Solution()
leng = answer.removeDuplicates(nums)
print(nums)
for i in range(0,leng):
    print(nums[i])

