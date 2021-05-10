#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 테스트 케이스 일부 불통과 (시간때문인듯)
def solution(progresses, speeds):
    temp = 0
    queue = progresses
    answer = []
    while(len(queue)>0):
        for i in range(len(queue)):
            queue[i] +=  speeds[i]
        for i in range(len(queue)):
            if(queue[0] >= 100):
                queue.pop(0)
                temp += 1
            else:
                break
        if(temp>0):
            answer.append(temp)
            temp = 0
    return answer
solution([93, 30, 55], [1, 30, 5])


# In[74]:


def solution2(progresses, speeds):
    answer = []
    time = 0
    count = 0  
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100: 
            progresses.pop(0)
            speeds.pop(0)
            count += 1
            
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer
solution2([93, 30, 55], [1, 30, 5])

