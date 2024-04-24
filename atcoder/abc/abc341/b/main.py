import bisect
import itertools
import sys
from typing import List

N = int(input())
A = list(map(int, input().split()))
for i in range(N-1):
    S, T = map(int, input().split())
    A[i+1] += T * (A[i]//S)
print(A[-1])
