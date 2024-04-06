import bisect
import itertools
import sys
from typing import List

T = input()
N = int(input())
bags = []

for _ in range(N):
    A_i, *S_i = input().strip().split()
    bags.append(S_i)

dp = [float("inf")] * (len(T) + 1)
dp[0] = 0

for i in range(N):
    dp_i = dp[:]
    for s in bags[i]:
        for j in range(len(T) + 1):
            if T.startswith(s, j):
                last = j + len(s)
                if last <= len(T):
                    dp_i[last] = min(dp_i[last], dp[j] + 1)
    dp = dp_i

ans = dp[len(T)]
if ans != float("inf"):
    print(ans)
else:
    print(-1)
