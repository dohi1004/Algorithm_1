#!/usr/bin/env python
# coding: utf-8

# #### 수식 최대화
# 
# 연산은 +, -, * 으로만 이루어짐
# 
# 우선 순위를 자유롭게 재정의하여 가장 큰 숫자 제출 (절댓값)
# 
# 입력: 수식
#     
# 출력: 최대화된 수식 결과

# In[114]:


from itertools import permutations
def solution(expression):
    operator = ['+','-','*']
    number = []
    temp = ''
    resultlist = []
    tmp = []
    
    # 가능한 연산자 조합
    combinations = list(permutations(['+','-','*'],3))

    # 연산 function
    def operation(num1,num2,op):
        if op == '*':
            return num1 * num2
        elif op == '-':
            return num1 - num2
        elif op == '+':
            return num1+num2

    # 숫자, 연산자 구분해서 리스트로 저장
    for i in expression:
        if i in operator:
            number.append(int(temp))
            number.append(i)
            temp = ''
            continue
        else:
            temp += i
    number.append(int(temp))
    tmp = number[:]
    stack = []
    result = []

    for op in combinations: # 전체 조합 확인
        for j in op: # [+,-,*] 이면 각 연산자 하나씩 우선순위에 따라 확인
            while True:
                if len(number) == 0: # 한바퀴 다 확인 -> 끝
                    break
                now = number.pop(0)
                if now == j: # 해당 연산자 발견 시 -> stack 제일 위 숫자와 tmp 제일 처음 숫자 연산 후 다시 스택에 담기
                    stack.append(operation(stack.pop(-1),number.pop(0),now))
                else: # 숫자 = 스택에 담기
                    stack.append(now)
            resultlist.append(int(stack[-1])) 
            # 그 다음 연산자로 가기 위함
            number = stack
            stack = []
        result.append(abs(int(resultlist[-1]))) # 최종 연산 결과
        # 초기화
        resultlist = []
        number = tmp[:]
    return max(result) # 최대값 출력

