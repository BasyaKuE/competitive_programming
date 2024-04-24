import bisect
import itertools
import sys
from typing import List

A, B = map(int, input().split())
if A+B == 1:
    print(0)
else:
    print(1)
