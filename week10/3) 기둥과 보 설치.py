#!/usr/bin/env python
# coding: utf-8

# ### 기둥과 보 설치
# 입력받은 build_frame에서 각 operation을 진행하고, 수행 후 조건을 만족하지 않으면 해당 수행을 하지 않고, 만족하면 해당 수행을 진행한다. 모든 수행들이 끝난 후 최종 결과물을 return
# 
# #### 조건: 
# 1. 기둥은 바닥 위 or 보의 한쪽 끝 위 or 또 다른 기둥 위
# 2. 보는 한쪽 끝이 기둥 위 or 양쪽 끝 다른 보와 동시 연결
# 
# 
# #### 입력: build_frame [x,y,a,b] [가로좌표, 세로좌표, 구조물 종류(기둥=0.보=1), 수행할 것(삭제=0, 설치=1)]
# #### 출력: [x,y,a]

# In[4]:


# 전체 확인
def check(result):
    for x, y, build in result:
        if build == 0: # 기둥  
            # 바닥 위 or 기둥 위 or 보의 한쪽 끝 위 (기둥 왼쪽 위치, 오른쪽 위치)
            if y == 0 or ([x,y-1,0] in result) or ([x,y,1] in result) or ([x-1,y,1] in result):
                continue
            return False # 하나라도 만족 못하면 구조 성립 안해
        elif build == 1: # 보
            # 한쪽 끝이 기둥 위 (왼쪽, 오른쪽) or 양쪽 끝 다른 보와 동시 연결
            if ([x,y-1,0] in result) or ([x+1,y-1,0] in result) or ([x-1,y,1] in result and [x+1,y,1] in result):
                continue
            return False
    return True # 다 끝나면 (모두가 만족) -> true

def solution(n, build_frame):
    result = []
    for frame in build_frame:
        x, y, build, op = frame
        if op == 0: # 삭제
            result.remove([x,y,build]) # 우선 삭제 해보기
            if not check(result): # 수행 후 말이 안되는 경우
                result.append([x,y,build]) # 다시 삭제한거 되돌리기
        elif op == 1: # 설치
            result.append([x,y,build]) # 우선 설치 해보기
            if not check(result): # 수행 후 말이 안되는 경우
                result.pop()
    return sorted(result)

