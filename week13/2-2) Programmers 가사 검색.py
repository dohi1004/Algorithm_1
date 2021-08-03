#!/usr/bin/env python
# coding: utf-8

# #### 가사 검색
# 
# 키워드 배열이 주어지면 해당 키워드로 단어 배열안에 있는 단어 중 몇개의 수를 만들 수 있는가?
# 
# 키워드는 와일드 카드 문자를 하나 이상 포함하고 있으며, 이 문자는 접두사 또는 접미사 중 하나로만 주어짐
# 
# ex) fro?? , ???st
# 
# 단어는 중복 x, 키워드는 중복 가능함
# 
# 입력: 단어 배열, 키워드 배열
# 
# 출력: 매치되는 가사 단어 수

# In[11]:


# 특정 단어의 길이를 기준으로 트라이 구조 생성 ex) 길이 5인 단어끼리 트라이 구조 1개 생성
# 해당 트라이 구조에서 단어가 들어올 때 각 문자별로 count를 1증가시키면 따로 탐색없이 개수 바로 셀 수 있음 
# ex) frodo, frost -> f = 2, r = 2, o = 2, d = 1, o = 1, s = 1, t = 1
class Trie:
    def __init__(self):
        self.children = {}
        self.count = 0 
        
    def insert(self, word):
        node = self
        for ch in word: # 한 문자씩 보기
            node.count += 1
            if ch not in node.children: # children에 존재 안하면
                node.children[ch] = Trie()  # 새롭게 노드 저장하기
            node = node.children[ch] # 다음 자식 노드를 보기 위함
        node.count += 1 # leaf node 카운트 1 증가
        
    def search(self, word):
        node = self # 해당 길이 trie 구조의 root
        for ch in word:
            if ch == '?': # ?를 만나면 
                return node.count # 현재 노드의 count 반환
            if ch not in node.children: # 해당 문자 없는 경우
                return 0 # 0 반환
            node = node.children[ch] # 넘어가기
        
        
def solution(words,queries):
    TrieRoot = [Trie() for _ in range(10000)] # 트라이 구조 length별로 있을 것 -> 미리 최대 개수(만 개) 만큼 만들기
    reverse_TrieRoot = [Trie() for _ in range(10000)] # 뒤집은 것도 
    answer = []
    
    for word in words:
        TrieRoot[len(word)-1].insert(word) # 해당 단어 길이의 트라이 구조에 insert
        reverse_TrieRoot[len(word)-1].insert(word[::-1]) # 거꾸로도 똑같이 insert
        
    for query in queries:
        if query[0] != '?': # 접미사에 ? 있으면
            answer.append(TrieRoot[len(query)-1].search(query)) 
        else: # 만약 접두사에 ? 있으면
            answer.append(reverse_TrieRoot[len(query)-1].search(query[::-1]))
        
    return answer

