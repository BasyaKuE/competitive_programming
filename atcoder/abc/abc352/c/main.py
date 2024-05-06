import bisect
import itertools
import sys
import collections

N = int(input())
kyojin = []
for _ in range(N):
    A, B = map(int, input().split())
    kyojin.append([A, B, (B-A)])
s_kyojin = sorted(kyojin, key=lambda x: x[2])
ans = 0
for i in range(N):
    if i == N-1:
        ans += s_kyojin[i][1]
    else:
        ans += s_kyojin[i][0]
print(ans)
