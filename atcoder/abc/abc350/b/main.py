import bisect
import itertools
import sys

N, Q = map(int, input().split())
T = list(map(int, input().split()))
chk = [1 for _ in range(N)]
ans = N
for i in range(Q):
    if chk[T[i]-1] == 1:
        chk[T[i]-1] = 0
        ans -= 1
    else:
        chk[T[i]-1] = 1
        ans += 1
print(ans)
