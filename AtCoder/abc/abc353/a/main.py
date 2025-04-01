import bisect
import itertools
import sys
import collections

N = int(input())
H = list(map(int, input().split()))
chk = H[0]
for i in range(1, N):
    if chk < H[i]:
        print(i+1)
        exit()
print("-1")
