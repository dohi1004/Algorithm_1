#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### 배열에서 주어진 구간만큼을 보면서 가장 큰 수와 작은 수의 차를 최소화하기

입력: 배열, 구간 길이
    
출력: 제일 작은 차이


# In[2]:


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l = 0
        r = k-1 
        length = len(nums)
        nums.sort() # 정렬 (비슷한 수끼리 빼야 차이가 더 작으므로)
        result = int(1e9) # 무한으로 초기화
        while r < length: # 끝까지 볼 때까지
            result = min(result, nums[r]-nums[l]) # 구간을 하나씩 이동해보며 최소화된 값 찾기
            l += 1
            r += 1
        return result    
        

