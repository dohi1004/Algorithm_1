#!/usr/bin/env python
# coding: utf-8

# #### 문자열에서 최대 홀수 찾기
# 
# ex) 
# 
# "52" -> "5"
# 
# "4206" -> " "
# 
# "35427" -> "35427"

# In[30]:


class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        length = len(num)
        if int(num[-1]) % 2 == 0: # 짝수인경우
            for i in range(1,length): 
                if(int(num[-1-i]) % 2 == 0): # 맨 뒤 하나씩 올려가면서 확인(짝수면 뛰어넘고)
                    continue
                else:
                    return num[-length:-i] # 홀수면 return
            
            return ""

        else: # 홀수면 그대로 return
            return num

