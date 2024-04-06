import bisect
import itertools
import sys
from typing import List
from bisect import bisect_left

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))

Q = int(input())
X = list(map(int, input().split()))

AB_sum = sorted({a + b for a in A for b in B})

for x in X:
    chk = False
    for c in C:
        need = x - c
        idx = bisect_left(AB_sum, need)
        if idx < len(AB_sum) and AB_sum[idx] == need:
            chk = True
            break
    print("Yes" if chk else "No")
