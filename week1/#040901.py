#!/usr/bin/env python
# coding: utf-8

# 1) 중복이 없는가 : 문자열이 주어졌을 때, 이 문자열에 같은 문자가 중복되어 등장하는지 확인하는 알고리즘. (자료구조를 추가로 사용하지않고 풀 수 있는 알고리즘도 고민)

# In[7]:


string1 = "helloworld"
string2 = "bye"

set1 = set(string2)
list1 = list(string2)

len1 = len(set1)
len2 = len(list1)

if(len1 != len1):
    print("같은 문자가 중복되어 있습니다")
else:
    print("중복된 문자가 없습니다")

