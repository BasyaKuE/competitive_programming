import bisect
import itertools
import sys
from typing import List

N = int(input())
P = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    A, B = map(int, input().split())
    if P.index(A) < P.index(B):
        print(A)
    else:
        print(B)
