import bisect
import itertools
import sys
from typing import List

N, A, B = map(int, input().split())
D = list(map(int, input().split()))
dp = [0 for _ in range(max(D))]  # 1なら休日, 0なら平日
# 初期状態
for i in range(A):
    dp[i] = 1

for i in range(1, N):
