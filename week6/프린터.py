#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def solution(priorities, location):
    count = 0
    while (len(priorities) != 0):
        if(location == 0):
            if priorities[0] < max(priorities): # 우선순위 내가 제일 안 커
                priorities.append(priorities.pop(0)) # 나보다 우선순위 큰 애 있으면 내 뒤로
                location = len(priorities) - 1 # 내가 맨끝에 갔으니 location 다시 업데이트
            else:
                return count+1 # 내가 우선 순위 제일 높아 -> 나 return
        else: 
            if(priorities[0] < max(priorities)): # 제일 앞이 우선순위 제일 안 높아
                priorities.append(priorities.pop(0)) # 뒤로 보내
                location -= 1 # 전체 한칸 앞으로 갔다고 생각
            else: # 제일 앞이 우선순위 제일 높아
                priorities.pop(0) # 걔 빼고
                location -= 1 # 다같이 한칸 앞으로
                count += 1 # 걔 출력했으니 카운트 증가

