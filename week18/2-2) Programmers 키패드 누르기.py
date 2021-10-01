#!/usr/bin/env python
# coding: utf-8

# #### 키패드 번호 주어졌을 때 어느 손가락으로 누르는지 반환하기
# 
# https://programmers.co.kr/learn/courses/30/lessons/67256 (그림 참고)
#     
# 왼쪽 줄 = 왼손, 오른쪽 줄 = 오른손, 중간 = 더 가까운 손가락이 움직임 
# 
# 같은 거리 이면 어느 손잡이냐에 따라 결정
# 
# 입력: 키패드 번호
#     
# 출력: 키패드 누르는 손가락 번호

# In[79]:


# bfs -> 일부 테스트 케이스 실패
def solution(numbers, hand):
    right = '#'
    left = '*'
    result = ''

    righthand = [3, 6, 9]
    lefthand = [1, 4, 7]

    #key: 키패드의 숫자, value: numi에서 i와 key 사이의 거리
    num2 = {1:1, 2:0, 3:1, 4:2, 5:1, 6:2, 7:3, 8:2, 9:3, 0:3, '#':4, '*':4}
    num5 = {1:2, 2:1, 3:2, 4:1, 5:0, 6:1, 7:2, 8:1, 9:2, 0:2, '#':3, '*':3}
    num8 = {1:3, 2:2, 3:3, 4:2, 5:1, 6:2, 7:1, 8:0, 9:1, 0:1, '#':2, '*':2}
    num0 = {1:4, 2:3, 3:4, 4:3, 5:2, 6:3, 7:2, 8:1, 9:2, 0:0, '#':1, '*':1}

    for i in numbers:
        if i in righthand:
            result += 'R'
            right = n
        elif i in lefthand:
            result += 'L'
            left = n

        else: # 2,5,8,0 경우
            if i == 2:
                distL = num2[left]
                distR = num2[right]
            elif i == 5:
                distL = num5[left]
                distR = num5[right]
            elif i == 8:
                distL == num8[left]
                distR = num8[right]
            else:
                distL == num0[left]
                distR == num0[right]
                
            if distL > distR:
                result += 'R'
                right = i
            elif distL < distR:
                result += 'L'
                left = i
            else:
                if hand == 'right':
                    result += 'R'
                    right = i
                if hand == 'left':
                    result += 'L'
                    left = i

    return result


# In[94]:


# 거리 딕셔너리로 정의 후 진행 -> 성공
def solution(numbers, hand):
    right = '#'
    left = '*'
    result = ''
    distL = int(1e9)
    distR = int(1e9)

    righthand = [3, 6, 9]
    lefthand = [1, 4, 7]

    #key: 키패드 번호 , value: 키패드 번호와 다른 버튼 사이 거리
    num2 = {1:1, 2:0, 3:1, 4:2, 5:1, 6:2, 7:3, 8:2, 9:3, 0:3, '#':4, '*':4}
    num5 = {1:2, 2:1, 3:2, 4:1, 5:0, 6:1, 7:2, 8:1, 9:2, 0:2, '#':3, '*':3}
    num8 = {1:3, 2:2, 3:3, 4:2, 5:1, 6:2, 7:1, 8:0, 9:1, 0:1, '#':2, '*':2}
    num0 = {1:4, 2:3, 3:4, 4:3, 5:2, 6:3, 7:2, 8:1, 9:2, 0:0, '#':1, '*':1}

    for i in numbers:
        if i in righthand: # 오른손이 누르는 경우
            result += 'R'
            right = i
        elif i in lefthand: # 왼손이 누르는 경우
            result += 'L'
            left = i

        else: # 2,5,8,0 경우
            if i == 2:
                distL = num2[left]
                distR = num2[right]
            elif i == 5:
                distL = num5[left]
                distR = num5[right]
            elif i == 8:
                distL = num8[left]
                distR = num8[right]
            else:
                distL = num0[left]
                distR = num0[right]

            if distL > distR:
                result += 'R'
                right = i
            elif distL < distR:
                result += 'L'
                left = i
            else:
                if hand == 'right':
                    result += 'R'
                    right = i
                if hand == 'left':
                    result += 'L'
                    left = i
    return result


# In[ ]:


LRLLRRLLLRR

