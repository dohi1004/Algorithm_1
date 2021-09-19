#!/usr/bin/env python
# coding: utf-8

# #### k번째로 큰 정수 찾기
# 
# ex) ["1","4","5","2"], k = 2
# 
# 5 -> 4 -> 2 -> 1
# 
# answer: 4 
# 
# 입력: nums 리스트, k
#     
# 출력: k번째로 큰 정수

# In[3]:


class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        temp = list(map(int,nums)) # 정수로 변환
        temp.sort() # 정렬
        return str(temp[-k]) # 문자로 변환

