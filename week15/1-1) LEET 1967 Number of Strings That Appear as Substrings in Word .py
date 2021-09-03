#!/usr/bin/env python
# coding: utf-8

# #### 단어 안에서 한 문자열이 나타나는 수 세기
# 
# word가 주어지면 그 안에서 patterns의 substring들이 나타나는지 확인 후 나타나면 카운트하기
# 
# ex) 
# 
# Input: patterns = ["a","abc","bc","d"], word = "abc"
# Output: 3
# 
# 입력: patterns, word
# 출력: word에 포함되는 patterns의 substring 수

# In[3]:


class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        count = 0
        for i in patterns:
            if i in word:
                count += 1
            else:
                continue
        return count    

