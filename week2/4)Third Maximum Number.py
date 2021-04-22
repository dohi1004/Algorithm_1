#!/usr/bin/env python
# coding: utf-8

# Third maximum number

# In[37]:


class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sorted_nums = sorted(nums)
        reverse_sorted_nums = sorted(nums, reverse = True)
        past = reverse_sorted_nums[0]
        count = 1
        result = 'null'
        for i in reverse_sorted_nums:
            if(past == i):
                continue
            else:
                count += 1
                past = i
                if(count == 3):
                    result = i
                    break

        if(result == 'null'):
            result = sorted_nums[-1]
        return(result)

nums = [1,2,3]
answer = Solution()
answer.thirdMax(nums)

