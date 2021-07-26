#!/usr/bin/env python
# coding: utf-8

# #### begin -> target으로 단어 변환하기 위한 최단 변경 횟수
# 
# <규칙>
# 
# 1. 한 번에 한 개의 알파벳만 변경 가능
# 
# 2. words에 있는 단어로만 변경 가능
# 
# <제한>
# 
# 반환할 수 없는 경우 0 return
# 
# begin과 target은 같지 않음
# 
# 등등..
# 
# 
# 입력: begin, target, words 리스트
# 
# 출력: 최소 몇 단계의 과정을 거쳐 변환이 가능한가? (횟수)

# In[14]:


# 단어가 한 자리수만 차이나는지 확인
def go(word1,word2): 
    count = 0
    for i in range(len(word1)):
        if word1[i] != word2[i]:
            count += 1
    return count == 1

def solution(begin, target, words):
    answer = [] 
    if target not in words: # target 없는 경우 0 리턴
        return 0
    # target에서 한 알파벳씩만 바꾸면서 begin으로 갈 수 있는지 확인 
    def dfs(target, words, depth):
        for word in words:
            if word == target and go(begin, word): # 하나 바꿔서 begin과 같아지는 경우 
                answer.append(depth) # 1 answer에 추가 후 끝
            elif go(target, word): # 한 글자 차이면
                dfs(word, [w for w in words if w != target], depth+1) # 그 단어 기준 target없는 wordlist에서 dfs 실행 
        
    dfs(target, words, 1)
    
    # answer의 값 중 최솟값을 반환 
    return min(answer)

