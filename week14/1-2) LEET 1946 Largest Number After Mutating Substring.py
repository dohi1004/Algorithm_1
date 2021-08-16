#!/usr/bin/env python
# coding: utf-8

# #### 변경을 선택하여 가장 큰 숫자 만들기
# 
# digit d ->(map) digit change[d]
# 
# ex) num = '132', change = [9,8,5,0,3,6,4,2,6,8]
# 
# 1을 바꾼다고 하면 change[1] = 8이므로 832가 됨 
# 변경 여부는 선택 가능함
# 
# single substring 단위로 변경 가능
# 
# 입력: num(문자열, 큰 정수 나타냄), change(길이 10 배열, 0~9를 다른 자릿수에 map)
#     
# 출력: 만들어진 최대 숫자

# In[68]:


class Solution:
    def maximumNumber(self, num: str, change: List[int]) -> str:
        
        num_list = list(num) # num 리스트에 담기
        changed = False # 변경된 여부 체크 위함
        
        for idx, d in enumerate(num_list): 
            val = int(d) # 해당 숫자를 change 인덱스로 찾기 위함
            if val < change[val]: # change에 있는 값이 더 크면
                changed = True
                num_list[idx] = str(change[val]) # 해당 값으로 변경
            elif changed and val > change[val]: # 변경된 적 있고, 지금 값이 더 큰 경우
                break # 멈추기
        return "".join(num_list) # string으로 변경

