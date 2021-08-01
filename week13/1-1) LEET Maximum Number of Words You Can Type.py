#!/usr/bin/env python
# coding: utf-8

# #### 최대로 타이핑 가능한 단어 수 반환
# 
# brokenLetters에 있는 단어는 타이핑 불가능 -> text의 단어가 이 letter 포함 시 타이핑 불가능
# 
# 입력: text, brokenLetters
# 
# 출력: 최대로 타이핑 가능한 단어 수 

# In[3]:


class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        text_list = text.split()
        count = len(text_list)
        for i in text_list: # 단어
            for j in brokenLetters: # 타이핑 불가능한 글자
                if j in i: # 불가능한 글자 포함시
                    count -= 1 # 못쳐
                    break

        return count

