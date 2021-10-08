#!/usr/bin/env python
# coding: utf-8

# #### 주어진 구간에서 모든 보석을 다 포함하는 가장 짧은 리스트 반환하기
# 
# 입력: 보석 리스트
#     
# 출력: 가장 짧은 구간

# In[1]:


gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]


# In[ ]:


def solution(gems):
    answer = [] 
    shortest = len(gems)+1 # 현재 최단 구간 길이

    start = 0 
    end = 0 

    check_len = len(set(gems)) # 보석의 총 종류 수
    gemcount = {} # 현재 구간에 포함된 보석들(종류: 갯수)

    while end < len(gems): # 끝까지 갈때까지
        gemcount[gems[end]] = 1 + gemcount.get(gems[end],0)           
        end += 1 # 끝 점 증가

        if len(gemcount) == check_len: # 모든 종류 확인 시
            while start < end: # start를 end로 옮기며 최소 구간 찾기
                if gemcount[gems[start]] > 1: # 하나씩 제거
                    gemcount[gems[start]] -= 1 
                    start += 1 
                    
                elif shortest > end - start: # 최단 거리 갱신
                    shortest = end - start
                    answer = [start+1, end]
                    break
                    
                else: # 한 종류라도 다 빠지면 끝
                    break
    


    return answer

