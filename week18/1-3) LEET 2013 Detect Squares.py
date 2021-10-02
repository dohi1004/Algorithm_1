#!/usr/bin/env python
# coding: utf-8

# #### 주어진 function에 따라 축이 평행한 사각형 개수 세기
# 
# DetectSquares() -> 초기화
# 
# add() -> 좌표 추가
# 
# count() -> 사각형 개수 세기
# 
# 
# 입력: function, 좌표
#     
# 출력: count -> 개수

# In[1]:


func = ["DetectSquares", "add", "add", "add", "count", "count", "add", "count"]

point = [[], [[3, 10]], [[11, 2]], [[3, 2]], [[11, 10]], [[14, 8]], [[11, 2]], [[11, 10]]]


# In[ ]:


class DetectSquares:

    def __init__(self):
        self.ptsCount=defaultdict(int)
        self.pts=[]
    def add(self, point: List[int]) -> None:
        self.ptsCount[tuple(point)]+=1 # 해당 점의 개수 세기
        self.pts.append(point) # 점 추가하기
    def count(self, point: List[int]) -> int:
        res=0
        px,py=point[0],point[1] # 새로 들어온 점
        for x,y in self.pts: # 현재 저장되어있던 점들 보기
            if (x==px and y==py) or abs(px-x)!=abs(py-y): # 만약 완전히 똑같은 점이거나 x와 y간의 거리가 다르면 넘어가기
                continue
            # 대각선 거리에 있는 점 고정하고 나머지 점들이 있는지 확인
            res+=self.ptsCount[(x,py)] * self.ptsCount[(px,y)] # 같은 축에 있는 점의 개수 세기
        return res

