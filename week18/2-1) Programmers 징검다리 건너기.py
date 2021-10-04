#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#### 징검다리 건널 수 있는 최대 수

디딤돌 숫자는 한 번 밟을 때마다 -1

디딤돌 숫자가 0이되면 더 이상 밟을 수 없으며, 이 때는 그 다음 돌로 여러칸 건너 뛸 수 있음

단, 다음 밟을 돌이 여러개 -> 가장 가까운 돌 밟음

입력: stones 배열, 디딤돌 최대 칸수
    
출력: 징검다리 건널 수 있는 최대 명수


# In[ ]:


def solution(stones, k):
    INF=int(1e9)
    start=1
    end=INF
    while(start<=end):
        mid=(start+end)//2 # 이분 탐색
        cnt=0
        flag=True
        for i in range(len(stones)): # 전체 stone에 대해서 mid 값으로 뺐을 때 0보다 작거나 같으면 cnt 증가 
            if stones[i]<=mid: # 연속된 0의 개수 찾기
                cnt+=1 
            else: cnt=0  # 연속되지 않으면 다시 카운트 초기화
            if cnt>=k: # 연속된 0 개수가 k 보다 크면 뛰어 넘을 수 없음을 의미
                flag=False # mid값 바꿔야함 (왼쪽으로) 
                break
        if not flag: 
            end=mid-1 # mid 하나 줄이기
        else:
            start= mid+1 # mid 하나 늘리기 (더 갈 수 있는 상태)
    return start

