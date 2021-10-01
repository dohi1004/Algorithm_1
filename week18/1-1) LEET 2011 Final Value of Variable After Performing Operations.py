#!/usr/bin/env python
# coding: utf-8

# #### 연산 후 결과값 출력하기
# 
# x++ , ++x = 1 증가
# x--, --x = 1 감소
# 
# 입력: operations
#     
# 출력: 최종 결과

# In[1]:


class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        x = 0
        for i in operations:
            if '-' in i:
                x -= 1
            if '+' in i:
                x += 1
        return x
        

