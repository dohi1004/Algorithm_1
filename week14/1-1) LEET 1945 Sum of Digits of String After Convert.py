#!/usr/bin/env python
# coding: utf-8

# #### 숫자로 변환 후 자릿 수 주어진 횟수 만큼 합하기
# 
# a\~z = 1~26이며, k 횟수 만큼 transform을 실시한다. 
# ex) s = abc, k = 1 
# convert: abc -> 123
# transform #1: 1 + 2 + 3 = 6
# 
# 입력: s(문자열) , k(repeat 횟수)
# 
# 출력: 결과값

# In[29]:


class Solution:
    def getLucky(self, s: str, k: int) -> int:
        convert = ''
        temp = 0

        for i in range(len(s)):
            convert += str(ord(s[i]) - 96) #아스키 코드 변환 후 1부터 시작하도록
            
        for i in range(k):# k번 반복
            for j in convert:  # convert 한 자릿수씩 돌면서
                temp += int(j) # 더해나가고
            convert = str(temp) # 더해진 결과 convert에 넣고
            temp = 0 # temp 초기화 
            
        return convert
        

