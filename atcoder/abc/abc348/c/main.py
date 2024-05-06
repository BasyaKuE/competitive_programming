import bisect
import itertools
import sys
from typing import List
from collections import defaultdict

N = int(input())
d = defaultdict(list)
for _ in range(N):
    A, C = map(int, input().split())
    d[C].append(A)
c = 0
for k, v in d.items():
    # print(min(v), v, k)
    if c <= min(v):
        c = min(v)
print(c)
