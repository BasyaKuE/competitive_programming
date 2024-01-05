import bisect
import itertools
import sys
from typing import List

N, S, K = map(int, input().split())
s: int = 0
for _ in range(N):
    P, Q = map(int, input().split())
    s += P*Q
if s >= S:
    print(s)
else:
    print(s+K)
