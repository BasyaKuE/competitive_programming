import bisect
import itertools
import sys
from typing import List

# 総和から引くみたいな感じ
N, K = map(int, input().split())
A = list(map(int, input().split()))

total = K * (K + 1) // 2
A_total = sum(set(num for num in A if num <= K))
ans = total - A_total

print(ans)
