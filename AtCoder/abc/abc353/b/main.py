import bisect
import itertools
import sys
import collections

N, K = map(int, input().split())
A = list(map(int, input().split()))
cnt = 0
now = 0
for i in range(N):
    if now + A[i] <= K:
        now += A[i]
    else:
        cnt += 1
        now = 0
        now += A[i]
if now == 0:
    print(cnt)
else:
    print(cnt+1)
