#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# [[0, 3], [1, 9], [2, 6]]
def solution(jobs):
    length = len(jobs)
    jobs = sorted(jobs, key = lambda x: x[1]) #소요 시간에 맞게 정렬(# [[0, 3], [2, 6], [1, 9]])
    time = 0 # 총 걸린 작업 시간
    clock = 0 # 현재 시간
    
    while(len(jobs) != 0): # jobs 있을 때 까지
        for i in range(len(jobs)): 
            if(jobs[i][0] <= clock): # 작업이 가능한 경우
                clock += jobs[i][1] # 현재시간 업데이트 0 -> 3 // 3 
                time += clock - jobs[i][0] # 작업시간 업데이트 (현재시간 - 내 시작시간)
                jobs.pop(i) # 그 작업 끝났으니 뺀다
                break # 종료! (clock업데이트 후 다시 처음부터 봐야함)
            if i == len(jobs) - 1: # 시작가능한 작업이 없어
                clock += 1 # 현재시간 1씩 update

    return (time//length)

