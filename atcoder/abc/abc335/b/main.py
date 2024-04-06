import bisect
import itertools
import sys
from typing import List

N: int = int(input())
for x in range(N+1):
    for y in range(N+1):
        for z in range(N+1):
            if x+y+z <= N:
                print(x, y, z)
