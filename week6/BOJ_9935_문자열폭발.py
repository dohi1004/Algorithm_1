#!/usr/bin/env python
# coding: utf-8

# In[28]:


text=input() # 문자열
bomb=input() # 폭발 문자열

ans=[]

for i in text:
    ans.append(i) # 문자열 스택에 넣기
    if ans[-1] == bomb[-1]:   # 마지막 넣은 값이 bomb의 마지막과 일치하면 앞을 봐
        if len(ans)>=len(bomb): # bomb보다 현재 스택안이 더 긴지 확인
            if(''.join(ans[-len(bomb):]) == bomb): # 맞으면 뒤부터 bomb 길이 앞만큼 문자열 확인해서 bomb랑 같은지 확인
                a=0
                while a<len(bomb): #bomb의 길이만큼 pop
                    ans.pop()
                    a+=1

#길이가 0이면 FRULA
if len(ans)==0:
    print("FRULA")
else:
    str=""
    for i in ans:
        str+=i
    print(str)

