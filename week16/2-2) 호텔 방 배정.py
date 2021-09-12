#!/usr/bin/env python
# coding: utf-8

# #### 주어진 방 리스트를 보고 최종 방 배정한 결과 반환
# 
# room_number 리스트가 주어진 상태에서 비어있는 경우 방을 배정해주고, 비어있지 않으면 그 수보다 큰 것 중 가장 작은 번호에 배정
# 
# 입력: 방 개수, 방 번호 요구사항
#     
# 출력: 최종 방 배정 번호

# In[9]:


# 1) 효율성 통과 x (시간 초과)
def solution(k, room_number):
    room = [-1] * (k+1)
    room = [-1] * (k+1)
    room_result = []
    pointer = 0
    for i in room_number:
        if room[i] == -1:
            room[i] = 0
            room_result.append(i)
        else:
            pointer = i
            for j in range(pointer+1,k+2):
                if room[j] == -1:
                    room[j] = 0
                    room_result.append(j)
                    break

    return room_result

# 2) 효율성 통과 x (시간 초과)
def solution(k, room_number):
    result = []

    for i in room_number:
        if i not in result:
            result.append(i)
        else:
            for j in range(i,k+1):
                if j not in result:
                    result.append(j)
                    break

    return result


# #### ex) 1 3 4 1 3 1
# 
# 1. 1번 방 비어있음 -> 1번 방 배정 (부모노드 = 2)
# 2. 3번 방 비어있음 -> 3번 방 배정 (부모노드 = 4)
# 3. 4번 방 비어있음 -> 4번 방 배정 (부모노드 = 5)
# 4. 1번 방 차있음 -> 부모노드인 2번방으로 가서 차있음으로 표시 (1,2의 부모노드 = 3)
# 5. 3번 방 차있음 -> 부모노드인 4번방 감, 4번방도 차있으니 부모노드인 5번방 감 (3,4,5의 부모노드 = 6)
# 6. 1번 방 차있음 -> 부모노드인 3번방 감, 3번방 차있음, 부모노드인 6번방 감 (1,3,6의 부모노드 = 7)

# In[11]:


# 효율성 통과
import sys
sys.setrecursionlimit(10000) # 재귀 리미트- 설정할 시 범위까지만 재귀 돈다

# 방문한 부모 노드 또한 업데이트 (전체 탐색 x)
def find(chk,rooms):
    if chk not in rooms: # 방 비어있으면 rooms에 기록(key), 그 다음 빈 방 value로 가지게 하기
        rooms[chk]=chk+1
        return chk # 비었던 방 번호 반환
    
    empty=find(rooms[chk],rooms)# 방이 안비어있으면, 재귀적으로 부모노드 찾기 
    # 빈방이 나오기 전 방문했던 부모 노드도 빈 방 다음 값으로 바꿔줌
    rooms[chk]=empty+1
    return empty

def solution(k,room_number):
    answer=[]
    # key = 차있는 방 번호, value = 다음 빈 방 번호 값
    rooms=dict()

    for i in room_number:
        temp=find(i,rooms) # 방번호와 딕셔너리 넣기
        answer.append(temp)

    return answer

