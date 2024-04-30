import bisect
import itertools
import sys
from typing import List

S = input()
T = input()

chk = ""
chk_i = 0
for i in range(len(S)):
    if S[i].upper() == T[chk_i]:
        chk += S[i]
        chk_i += 1
    if chk_i >= 3:
        break
# print(chk)
if chk.upper() == T or chk[0:2].upper()+"X" == T:
    print("Yes")
else:
    print("No")
