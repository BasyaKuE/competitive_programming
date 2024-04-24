import bisect
import itertools
import sys
from typing import List

N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
for i in range(N):
    ans = 0
    for j in range(N):
        chk = ((S[i][0] - S[j][0]) ** 2 + (S[i][1] - S[j][1]) ** 2) ** 0.5
        if chk > ans:
            ans = chk
            ans_i = j+1
    print(ans_i)
