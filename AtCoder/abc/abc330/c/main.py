import bisect
import itertools
import sys
import math
from typing import List

D: int = int(input())
ans: int = float("inf")
for x in range(1, math.isqrt(D)+1):
    y: int = x
    left: int = 0
    right: int = math.isqrt(D)
    while True:
        min = (left + right) // 2
        if min < 0:
            left = left + 1
        elif min >
