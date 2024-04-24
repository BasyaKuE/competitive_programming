import bisect
import itertools
import sys
from typing import List

N = int(input())
A = [list(map(int, input().split())) for _ in range(N)]
G = [[] for _ in range(N)]
for i in range(N):
    a = A[i]
    for j in range(N):
        if a[j] == 1:
            G[i].append(j+1)
for g in G:
    print(*g)
