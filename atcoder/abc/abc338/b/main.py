import bisect
import itertools
import sys
from typing import List

from collections import defaultdict

S = input()
d = defaultdict(int)
for ch in S:
    d[ch] += 1
chk = -1
ans = ord("z") + 1
# print(d)
for k, v in d.items():
    if v > chk:
        ans = ord(k)
        chk = v
    elif v == chk and ord(k) <= ans:
        ans = ord(k)
        chk = v
# print(chk)
print(chr(ans))
