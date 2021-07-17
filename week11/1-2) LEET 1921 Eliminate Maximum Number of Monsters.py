#!/usr/bin/env python
# coding: utf-8

# #### 몬스터 최대로 잡기
# 
# 처음에 총알은 장전되어 있고, 그 이후에는 장전하는데 1분 걸림 (즉, 한 턴에 한 몬스터 제거 가능)
# 
# 도시에 몬스터가 도달하면 loss => 이때까지 최대로 잡을 수 있는 몬스터 수를 return!
# 
# (1분 지날 때마다 (거리 - 스피드)로 다음 단계에 몬스터가 다가옴)
# 
# 
# 입력: 몬스터 거리, 몬스터 스피드
# 출력: 최대로 잡을 수 있는 몬스터 수

# In[59]:


class Solution(object):
    def eliminateMaximum(self, dist, speed):
        """
        :type dist: List[int]
        :type speed: List[int]
        :rtype: int
        """
        scene = []
        result = 0
        length = len(dist) # 총 몬스터 수
        scene = list(zip(dist,speed))
        time = [i/j for i,j in scene] # 도시에 도달하는데 걸리는 시간
        time.sort() # 시간 작은 순으로 정렬
        
        for i in range(length): # 총 몬스터 수만큼 반복
            if i >= time[i]:  # 만약 n 번째 분보다 time[i]가 더 작으면 끝 (n분보다 작은 것은 이미 도시 도달했음을 의미)
                return result 
            result += 1 # 아닌 경우 몬스터 한 마리 더 잡음
        return result # 최대로 잡은 경우

