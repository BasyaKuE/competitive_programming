import bisect
import itertools
import sys
from typing import List

S: str = input()
chk = set()
for i in range(len(S)):
    for j in range(i, len(S)):
        s = S[i:j+1]
        chk.add(s)
# print(chk)
print(len(chk))
