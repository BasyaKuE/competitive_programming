import bisect
import itertools
import sys
import collections

B, G = map(int, input().split())
if B > G:
    print("Bat")
else:
    print("Glove")
