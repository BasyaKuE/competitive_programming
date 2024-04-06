import bisect
import itertools
import sys
from typing import List

W, B = map(int, input().split())
S = "wbwbwwbwbwbw"*100

N = W+B
flag = False
for i in range(len(S)-N):
    T = S[i:N+i]
    # print(T)
    if T.count("w") == W and T.count("b") == B:
        flag = True
        break
if flag:
    print("Yes")
else:
    print("No")
