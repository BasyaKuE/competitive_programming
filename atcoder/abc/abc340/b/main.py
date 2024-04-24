import bisect
import itertools
import sys
from typing import List

Q = int(input())
A = []
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        A.append(query[1])
    else:
        print(A[-(query[1])])
