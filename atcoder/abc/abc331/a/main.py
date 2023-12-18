import bisect
import itertools
import sys
from typing import List

M, D = map(int, input().split())
y, m, d = map(int, input().split())

if M == m and D == d:
    print(y+1, 1, 1)
elif D == d:
    print(y, m+1, 1)
else:
    print(y, m, d+1)
