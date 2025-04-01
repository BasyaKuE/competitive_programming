import bisect
import itertools
import sys
import collections

N = int(input())
A = list(map(int, input().split()))
A.sort()
print(*A)
chk = [0 for _ in range(10**8 + 1)]
for a in A:
    chk[a] += 1

