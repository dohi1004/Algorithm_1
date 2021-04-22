#!/usr/bin/env python
# coding: utf-8

#  2)  문자열 회전 : 한 단어가 다른 문자열에 포함되어 있는지 판별하는 isSubstring이라는 메서드가 있다고 치자. s1 과 s2 두 문자열이 주어지고, s2가 s1을 회전시킨 결과인지 판별하고자 한다.

# In[46]:


from collections import deque
def isSubstring(s1,s2):
    deqs1 = []
    deqs2 = []
    result = "false"

    for i in s1:
        deqs1.append(deque(i))
    for i in s2:
        deqs2.append(deque(i))

    if(len(s1) != len(s2)):
        print("false")

    for i in range(len(s2)):
        if(deqs1 == deqs2):
            result = "true"
        else:
            rotate = deqs2.pop()
            deqs2.insert(0,rotate)

    print(result)
isSubstring("waterbottle","erbottlewat")

