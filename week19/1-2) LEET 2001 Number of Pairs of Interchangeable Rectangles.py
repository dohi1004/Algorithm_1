#!/usr/bin/env python
# coding: utf-8

# #### interchangeable 한 pair 수 세기
# 
# 사각형의 width/height가 같으면 interchangable
# 
# 입력: 사각형 리스트 
#     
# 출력: interchangeable한 pair 수

# In[1]:


rectangles = [[4,8],[3,6],[10,20],[15,30]]


# In[17]:


import itertools
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
   
        num = 0
        cb = itertools.combinations(range(0,len(rectangles)),2)
        def interchangable(square1,square2):
             return square1[0]/square1[1] == square2[0]/square2[1]    


        for c in cb:
            if interchangable(rectangles[c[0]],rectangles[c[1]]):
                num += 1
                
        return num 


# In[20]:


class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        answer = 0
        temp = {}

        for w,h in rectangles: # 딕셔너리에 해당 키에 겹치면 값 하나씩 늘려가며 저장
            temp[w/h] = 1 + temp.get(w/h,0)

        for i in temp.values():
            if i > 1: # 하나 이상 겹치는게 있었다면
                answer += (i * (i-1))//2 # 조합에서 2개 뽑는 것이랑 같음 (순서없이 2개 뽑기)
                
        return answer      

