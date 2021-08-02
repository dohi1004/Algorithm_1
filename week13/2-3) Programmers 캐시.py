#!/usr/bin/env python
# coding: utf-8

# #### LRU 캐시 구현
# 
# 캐시 교체 알고리즘 -> 가장 최근에 참조되지 않았던 단어 교체(LRU) 
# 
# cache hit = 1초, cache miss = 5초
# 
# 입력: 캐시 크기, 도시
#     
# 출력: 캐시 크기에 따른 실행 시간

# In[8]:


def solution(cacheSize, cities):
    length = len(cities)
    if(cacheSize == 0): # 캐시사이즈 0인 경우 모두 miss남
        return length * 5
    
    lower_cities = [i.lower() for i in cities] # 소문자로 변환
    cache = []
    time = 0
    
    for i in lower_cities:
        if len(cache) >= cacheSize: # 캐시 꽉차면
            if i in cache: # cache hit
                cache.remove(i)
                time += 1
            else: # cache miss
                cache.pop(0)
                time += 5
        else: # 캐시 빈 공간 있으면
            if i in cache: # cache hit
                cache.remove(i)
                time += 1
            else:
                time += 5 # cache miss
        cache.append(i)
    return time

