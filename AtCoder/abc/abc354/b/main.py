import bisect
import itertools
import sys
import collections

N = int(input())
A = []
T = 0
for _ in range(N):
    S, C = map(str, input().split())
    A.append(S)
    T += int(C)
A.sort()
ans = T % N
# print(A, ans)
print(A[ans])
