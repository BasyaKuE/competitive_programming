import bisect
import itertools
import sys
import collections

N, Q = map(int, input().split())
ans = 0
now_L, now_R = 1, 2
for _ in range(Q):
    H, T_str = map(str, input().split())
    T = int(T_str)
    if H == "R":
        if now_L < now_R < T or now_R < T < now_L:
            # 右回り
            ans += T-now_R
            now_R = T
        elif now_R < now_L < T or T

        # T < now_L < now_R
