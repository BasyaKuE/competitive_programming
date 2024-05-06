import bisect
import itertools
import sys
import collections

S = input()
T = input()
ans = []
S_i = 0
for i in range(len(T)):
    if S[S_i] == T[i]:
        ans.append(i+1)
        S_i += 1
print(*ans)
