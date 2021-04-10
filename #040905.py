#!/usr/bin/env python
# coding: utf-8

# 5) 문자열 압축 : 반복되는 문자의 개수를 세는 방식의 기본적인 문자열 압축 메서드를 작성하라. 예를 들어, 문자열 aabccccaaa 압축하면 a2b1c5a3이 된다. 만약 압축한 문자열의 길이가 기존 문자열의 길이보다 길다면 기존 문자열을 반환해야 한다. 문자열은 a-z 으로만 이루어져있다.

# In[52]:


def compression(string):
    result = ""
    temp = ""
    count = 1
    for i in range(len(string)):
        if(i+1 == len(string)):
            break
        if(string[i] == string[i+1]):
            count += 1
            temp = string[i]+str(count)
        else:
            temp = string[i]+str(count)
            result += temp
            temp = ""
            count = 1
    if(string[-1] != string[-2]):
        result += string[-1]+"1"
    result += temp

    if(len(result) > len(string)):
        print(string)
    else:
        print(result)
compression("aabcccccaaa")

