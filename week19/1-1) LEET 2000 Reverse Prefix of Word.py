#!/usr/bin/env python
# coding: utf-8

# #### 주어진 문자를 찾으면, 0번째 인덱스부터 거꾸로 돌려서 반환하기
# 
# 입력: word, ch
#     
# 출력: 최종 결과

# In[9]:


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        reverse = ''
        num = 0
        answer = ''
        temp = True

        for i in word: 
            reverse += i
            num += 1
            if i == ch: # 해당 단어 찾으면 멈추기
                temp = False
                break
        if temp:
            return word
            
        reverse = reverse[::-1] # 만약 존재한다면 거꾸로 돌리기
        answer = reverse + word[num:]
        return answer

