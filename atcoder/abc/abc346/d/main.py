import bisect
import itertools
import sys
from typing import List

def min_cost(n, s, c):
    INF = 10**18
    dp = [INF] * n
    char_val = [0 if s[i] == '0' else 1 for i in range(n)]
    for i in range(n):
        if i > 0:
            dp[i] = min(dp[i], dp[i-1] + c[i])
        dp[i] = min(dp[i], c[i] + sum(c[j] for j in range(i) if char_val[j] == char_val[i]))
    return min(dp[i] + sum(c[j] for j in range(i+1, n) if char_val[j] == char_val[i]) for i in range(n))

n = int(input().strip())
s = input().strip()
c = list(map(int, input().strip().split()))
print(min_cost(n, s, c))
