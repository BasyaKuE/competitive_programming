import bisect
import itertools
import sys
from typing import List

S: str = input()
T: str = input()

chk: List[str] = ["A", "B", "C", "D", "E"]
s_chk: int = abs(chk.index(S[0]) - chk.index(S[1]))
t_chk: int = abs(chk.index(T[0]) - chk.index(T[1]))
s_chk = min(s_chk, 5-s_chk)
t_chk = min(t_chk, 5-t_chk)
# print(s_chk, t_chk)
if s_chk == t_chk:
    print("Yes")
else:
    print("No")
