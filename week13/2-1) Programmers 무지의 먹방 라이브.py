#!/usr/bin/env python
# coding: utf-8

# #### 무지의 먹방 라이브
# 
# 회전판 음식 먹기 (음식 하나 1초 섭취 후 남기고, 다음 번호 남은 음식 섭취)
# 
# k초후 네트워크 장애 발생 -> 네트워크 정상화 후 몇번 음식부터 먹어야할까?
# 
# ex) [3,1,2], k =5
# 
# [3,1,2] -> [2,1,2] -> [2,0,2] -> [2,0,1] -> [1,0,1] -> [1,0,0] (5초) // 그 다음 먹을 번호 = 1번 음식
# 
# 남은 음식 없으면 -1 반환
# 
# 
# 입력: 음식 먹는데 필요한 시간(food_times), 네트워크 장애 발생한 시간(k)
# 
# 출력: 다시 섭취해야할 음식 번호

# In[ ]:


def solution(food_times, k):
    if sum(food_times) <= k: # 다 먹을 수 있는 경우
        return -1
    if len(food_times) > k: # 음식 많은 경우(한바퀴 안도는 경우)
        return k+1
    temp = []
    length = len(food_times)
    before = 0
    index = 0
    
    temp = list(enumerate(food_times))
    temp = sorted(temp, key = lambda a : a[1]) # 음식양 기준 정렬

    for i in range(length):
        compare = (temp[i][1]-before) * (length-i) # 최소값 * 길이 => 그 다음 턴에는 이전거 빼는 식으로 구현함(이미 먹은거니까)
        before = temp[i][1]
        if compare <= k: # 최소값만큼 뺄 수 있는 경우
            k -= compare
        else: # 아닌 경우 (k < 남은 음식 길이) # 한바퀴만 마지막으로 돌면 됨
            temp = sorted(temp[i:]) # 남은 음식 인덱스 순 정렬
            index = temp[k%len(temp)][0] # 남은 음식 중 먹어야할 음식 찾기 (k초후)
            return index+1 # 인덱스 0부터 시작이므로 1 더해서 반환

