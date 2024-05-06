import bisect
import itertools
import sys
import collections

N, X, Y, Z = map(int, input().split())
if Y <= Z <= X or X <= Z <= Y:
    print("Yes")
else:
    print("No")
