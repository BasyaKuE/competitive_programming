import bisect
import itertools
import sys
from typing import List

N: int = int(input())
A: List[int] = list(map(int, input().split()))
B: List[int] = sorted(A)
B_sum: List[int] = [0 for _ in range(N)]
B_sum[0] = B[0]
for i in range(1, N):
    B_sum[i] = B[i] + B_sum[i-1]
# print(*B_sum)
ans = []
S = sum(A)
for a in A:
    i = bisect.bisect_right(B, a)
    ans.append(S-B_sum[i-1])
print(*ans)
