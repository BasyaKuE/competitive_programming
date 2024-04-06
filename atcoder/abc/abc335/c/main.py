import bisect
import itertools
import sys
from typing import List

N, Q = map(int, input().split())
body = [0 for _ in range(N)]
for _ in range(Q):
    q1, q2 = map(str, input().split())
    if q1 == "1":
        
