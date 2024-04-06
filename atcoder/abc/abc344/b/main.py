import bisect
import itertools
import sys
from typing import List

rec = []
while True:
    A = int(input())
    if A == 0:
        rec.append(A)
        break
    else:
        rec.append(A)
for i in range(len(rec)):
    print(rec[-(i+1)])
