#!/usr/bin/env python
# coding: utf-8

# #### mxn 행렬의 각 레이어를 반 시계 방향으로 k번 회전시키기
# 
# m,n = 짝수 
# 
# 입력: 행렬, k
# 
# 출력: k번 회전 시킨 후 행렬

# In[139]:


a = [1,5,9,13,14,15,16,12,8,4,3,2]
a[-2:]


# In[137]:


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
            col = len(grid)
            row = len(grid[0])
            x = 0
            y = 0
              
            def rotate(grid, k, col, row):
                rotatetrial = 0
                length = 2 * (col + row - 2) # 가로 세로 더하고 겹친 부분 하나씩 뺀 다음 *2 (테두리 길이)
                temp = [0] * length # 테두리를 1차원 리스트에 저장
                index = 0
                
                # 테두리 부분만 temp에 담기 (x,y는 레이어마다 적용 위함)
                for a in range(col): # 첫 열은 밑으로 
                    temp[index] = grid[a+x][y] 
                    index += 1
                for b in range(1,row): # 맨 밑은 오른쪽으로 (시작 한칸 띄우고, 이미 밑에서 오는애가 채워놓음)
                    temp[index] = grid[col-1+x][b+y]
                    index += 1
                for c in range(1,col): # 밑에서 위로
                    temp[index] = grid[col-1-c+x][row-1+y]
                    index += 1
                for d in range(1,row-1): # 맨 위는 왼쪽으로
                    temp[index] = grid[x][row-1-d+y]
                    index += 1
                
                # 회전 시키기
                rotatetrial = k % length
                temp = temp[-rotatetrial:] + temp[0:len(temp)-rotatetrial]
                return temp
            
            # 회전된 레이어 원본에 붙이기
            def put(mat):
                index = 0
                for a in range(col):
                    grid[a+x][y] = mat[index] # 밑으로
                    index += 1
                for b in range(1,row): # 오른쪽
                    grid[col-1+x][b+y] = mat[index]
                    index += 1
                for c in range(1,col): # 위로
                    grid[col-1-c+x][row-1+y] = mat[index]
                    index += 1
                for d in range(1,row-1): # 왼쪽
                    grid[x][row-1-d+y] = mat[index]
                    index += 1

            while col > 0 and row > 0: # 마지막 안의 사각형 다 볼 때까지
                put(rotate(grid,k,col,row))
                col -= 2 # 짝수이므로
                row -= 2
                x += 1 # 다음 레이어 시작을 위해 1씩 더해 (0,0) -> (1,1) -> ..
                y += 1
            return grid  

