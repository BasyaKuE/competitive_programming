import bisect
import itertools
import sys
from typing import List

N, K = map(int, input().split())
A: List[int] = list(map(int, input().split()))
ans: List[int] = []
for i in range(N):
    if A[i] % K == 0:
        ans.append(A[i]//K)
print(*ans)
