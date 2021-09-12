#!/usr/bin/env python
# coding: utf-8

# #### 주어진 것과 리스트에 없는 이진수 반환하기
# 
# 입력: nums 리스트
#     
# 출력: 주어진 것에 존재하지 않는 unique한 이진수 

# In[25]:


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        length = len(nums)
        decimal = [int(i,2) for i in nums] # 십진수 변환
        
        for i in range(1 << length): 
            if i not in decimal: # 겹치지 않으면
                temp = bin(i)[2:] # 이진수로 변환 후
                return '0'*(length-len(temp)) + temp # 앞에 0 붙여서 반환     

