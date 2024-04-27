import bisect
import itertools
import sys
import collections

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(max(sum(A) - sum(B) + 1, 0))
