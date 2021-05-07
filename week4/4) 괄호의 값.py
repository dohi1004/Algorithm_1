#!/usr/bin/env python
# coding: utf-8

# https://www.acmicpc.net/problem/2504

# In[5]:


def brackets(bracket):
    stack = []
    temp = 1
    res = 0

    for i in range(len(bracket)):
        # 스택에 아무것도 없는데 닫는 괄호 오면 오류 -> 0 출력
        if bracket[i] == ']' or bracket[i] ==')':
            if not stack:
                print(0)
                return 0
        # 닫는괄호 '(' 의 경우 2 곱함 -> 만약 그 다음거에 )가 나오면 결과에 더함    
        if bracket[i] == '(':
            stack.append('(')
            temp = temp * 2
            if i + 1 < len(bracket) and bracket[i+1] == ')':
                res += temp
        # 닫는 괄호 '['의 경우 3곱하고 -> 그 다음거에 ]가 나오면 결과에 더함
        elif bracket[i] == '[':
            stack.append('[')
            temp = temp * 3
            if i + 1 < len(bracket) and bracket[i+1] == ']':
                res += temp
        
        # stack안에 닫는 괄호들 보면서 만나면 각 value로 나누고 여는괄호랑 만난 경우 스택에서 여는 괄호 뺌
        if stack:
            if bracket[i] == ')':
                temp = temp // 2
                if stack[-1] == '(':
                    stack.pop()
            elif bracket[i] == ']':
                temp = temp // 3
                if stack[-1] == '[':
                    stack.pop()
    # stack안에 남은 값있으면 0출력 (괄호 제대로 안된 상태)
    if len(stack) > 0:
        print(0)
        return 0
    # for문 다돌고 result 출력
    print(res)
    
bracket = str(input())
brackets(bracket)

