#!/usr/bin/env python
# coding: utf-8

#  2)  순열 확인 : 문자열 두 개가 주어졌을 때 이 둘이 서로 순열 관계에 있는지 확인하는 메서드를 작성하라.

# In[8]:


def checkpermutation(string1, string2):
    string2 = list(string2)
    if(len(string1) != len(string2)):
        print("False")
    else:
        for i in string1:
            for j in string2:
                if(i == j):
                    string2.pop(string2.index(j))
                    break
        if(len(string2) == 0):
            print("True")
        else:
            print("False")
            
checkpermutation("taco cat","acto cta")

