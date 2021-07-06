#!/usr/bin/env python
# coding: utf-8

# #### 배열 안 단어에서 특정 글자들을 옮겨서 모두가 같은 단어가 되도록 만들기
# 
# #### 가능하면 true return, 안되면 false return

# In[ ]:


words = ["abc","aabc","bc"] # true
words = ["ab","a"] # false


# #### words의 총 길이가 n일때, n의 배수 개수만큼 만큼 각 문자들이 존재한다면 이동으로 같아질 수 있음

# In[39]:


class Solution(object):
    def makeEqual(self, words):
        length = len(words) 
        if length == 1: # 한 문자인 경우 -> True
            return True 
        
        check = ''
        for i in words:
            check += i
            
        check2 = set(check) # 겹치는 거 모두 제외한 문자들
        if len(check2) == len(check): # a b c 이런 식으로만 존재하는 경우 같아질 수 x
            return False
        
        result = []
        for j in check2:
            result.append(check.count(j)) # check에서 unique한 문자들 개수 세기(a 몇개, b 몇개 ...)
        
        for k in result: # 각 문자들 개수가 words의 n의 배수만큼 존재하는가? (나머지 = 0)
            if k%length >= 1: 
                return False # 특정 문자 하나라도 n의 배수 아닌 경우 False
        return True # 모든 문자들이 다 words의 n 배수인 경우 True

