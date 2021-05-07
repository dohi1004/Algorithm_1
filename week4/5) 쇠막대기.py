#!/usr/bin/env python
# coding: utf-8

# https://www.acmicpc.net/problem/10799

# In[17]:


def brackets(bracket):
    stack = []
    res = 0

    for i in range(len(bracket)):
        # 닫는괄호 '(' 의 경우 1씩 더함(파이프 하나씩 생기는거)
        if bracket[i] == '(':
            stack.append('(')
        # 만약 바로 다음게 ')'이면 레이저니까 스택길이만큼더함(스택안의 막대기가 모두 레이저로 잘리면 하나씩 늘어남) 
        elif bracket[i] == ')':
            if bracket[i-1] == '(':
                stack.pop()
                res += len(stack)
            # 각 막대기의 끝부분 -> 막대기 끝이니 스택에서 빼고, 1더함(막대기 1개)  
            else:
                stack.pop()
                res += 1
        else: # 둘 중 아무것도 아닌 경우 -> 오류
            print(0)
            return 0

    # for문 다돌고 result 출력
    print(res)
    
bracket = str(input())
brackets(bracket)

