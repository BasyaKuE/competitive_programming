import bisect
import itertools
import sys
from typing import List

S: str = input()
chk: int = int(S[3:])
if chk == 0 or chk == 316 or chk >= 350:
    print("No")
else:
    print("Yes")
