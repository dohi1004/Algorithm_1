#!/usr/bin/env python
# coding: utf-8

# #### 이웃의 평균이 자신이 되지 않는 배열 만들기
# 
# ex)
# Input: nums = [1,2,3,4,5]
# Output: [1,2,4,5,3]
# 
# 입력: nums 리스트
# 
# 출력: 이웃의 평균이 자신이 되지 않는 배열

# In[25]:


# 시간 초과 -> 모든 경우의 수 구해서 되는 경우 뽑은 후 그 중 제일 앞에거 리턴

import itertools 
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        npr = list(itertools.permutations(nums, len(nums)))
        temp = []
        length = len(npr[0])
        flag = True
        for i in range(len(npr)):
            for j in range(1,length):
                if j+1 >= length:
                    break
                if (npr[i][j-1] + npr[i][j+1]) // 2 == npr[i][j]:
                    flag = False
                    break

            if flag is True:
                 temp.append(npr[i])
            else:
                flag = True


# In[ ]:


# 최대 최소 최대 최소 ... 순으로하면 평균값이 될 수 없다고 생각..!


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort() # 크기순 정렬
        minnum = 0
        maxnum = -1
        temp = []
        for i in range(len(nums)):
            if i % 2 != 0: # 홀수의 경우 최대값 배치
                temp.append(nums[maxnum])
                maxnum -= 1
            else: # 짝수의 경우 최솟값 배치
                temp.append(nums[minnum])
                minnum += 1
                
        return temp

