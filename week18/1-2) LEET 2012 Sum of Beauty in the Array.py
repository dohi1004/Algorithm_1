#!/usr/bin/env python
# coding: utf-8

# #### sum of beauty 구하기
# 
# 각 index i(1 <= i <= nums.length - 2)에 대해 
# 
# beauty of i는 다음과 같이 정의한다.
# 
# 2, if nums[j] < nums[i] < nums[k], for all 0 <= j < i and for all i < k <= nums.length - 1.
# 
# 1, if nums[i - 1] < nums[i] < nums[i + 1], and the previous condition is not satisfied.
# 
# 0, if none of the previous conditions holds.
# 
# 입력: nums
# 
# 출력: sum of beauty

# nums = [2,4,6,4]
# 
# numlist = [2,4,4,6]
# 
# i = 1,2
# 
# nums[i] = [2,[4,6],4]
# 
# 2 < 4 < 6,4 ?
# 
# 2,4 < 6 < 4 ?
# 
# 왼쪽의 최대보다 크고, 오른쪽의 최소 보다 작게!
# 
# 2 -> 패스 (current_max = 2)
# 
# 4 -> nums[i]이므로, 이전 것 중 최대 값보다 큰지 확인 + 이후의 최소값보다 작은지 확인 => 그렇다면 += 2 하기
# 
#   -> 조건 불만족 시, 1에 해당하는 조건 확인

# In[ ]:


# 시간 초과
class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        length = len(nums)
        numlist = sorted(nums)
        answer = 0

        current_max = 0

        for index, i in enumerate(nums):
            numlist.remove(i)  # nums[i] (뒤에 리스트만을 보기 위해 삭제시키기) => 시간초과 원인으로 보임 O(N)
            if 1 <= index <= length - 2: # index i인가?
                if current_max < i < numlist[0]: # 왼쪽에서 가장 큰 값보다 i가 크고, 오른쪽에서 정렬한 것 기준 제일 작은 값보다 작으면
                    answer += 2
                elif nums[index - 1] < i < nums[index+1]:
                    answer += 1
            current_max = max(current_max,i) # nums[i] 
        return answer
        


# In[ ]:


class Solution:
    def sumOfBeauties(self, nums: List[int]) -> int:
        minlist=[]
        minnum=int(1e9)
        for i in nums[::-1]: #거꾸로 시작해서 i위치까지 중 최솟값 찾기
            minnum=min(minnum,i)
            minlist.append(minnum)
        minlist=minlist[::-1] # 다시 원래상태로 [1,2,3(현재),4,5,6] 4,5,6의 최소는 맨 끝에 저장이 되기 때문
        ans=0
        maxnum=nums[0] # 제일 처음은 인덱스 0번부터 시작
        for i in range(1,len(nums)-1): 
            if maxnum < nums[i] < minlist[i+1]:
                ans+=2
            elif nums[i-1]< nums[i] < nums[i+1]:
                ans+=1
            maxnum=max(maxnum,nums[i])
        return ans  

