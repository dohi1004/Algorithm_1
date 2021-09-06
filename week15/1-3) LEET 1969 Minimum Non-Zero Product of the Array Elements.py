#!/usr/bin/env python
# coding: utf-8

# #### 배열의 숫자들의 곱으로 0이 아닌 최솟값 구하기
# 
# 배열에 주어진 숫자 비트로 표현했을 때 한자리씩 swapping -> 곱 최소로 만들기
# 
# 입력: p  [1, 2^p - 1]
# 
# 출력: 배열의 숫자들의 곱으로 0이 아닌 최솟값

# In[ ]:


class Solution: # (a*b) > (a+b-1) * 1
    def minNonZeroProduct(self, p: int) -> int:
        mod = 10 ** 9 + 7

        top = pow(2,p,mod) - 1 # pow(base,exp,mod) (base ** exp) % mod 
        mid = top - 1 # top -1 값으로 변경할 것
        midcount = pow(2,p-1) - 1 # top - 1 까지 기준 중간 값 (총 몇 개 나올지 결정됨)

        return (pow(mid, midcount, mod)* top) % mod # (mid * 1) 총 (midcount) 수만큼 나옴 * top        

