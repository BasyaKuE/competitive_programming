import bisect
import itertools
import sys
from typing import List

N = int(input())
S = bin(N).split("1")
print(len(S[-1]))
