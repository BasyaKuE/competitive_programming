import bisect
import itertools
import sys
from typing import List

N: int = int(input())
A: List[int] = list(map(int, input().split()))

left_chk: int = 0
for i in range(N//2):
    if left_chk < A[i]:
        left_chk += 1
    elif left_chk > A[i]:
        left_chk = A[i]

right_chk: int = 0
for i in range(N//2):
    if right_chk < A[-(i+1)]:
        right_chk += 1
    elif right_chk > A[-(i+1)]:
        right_chk = A[-(i+1)]

if N%2 == 0:
    
