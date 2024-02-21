import bisect
import itertools
import sys
from typing import List

N = int(input())
S = input()
T = input()

a_chk = [0 for _ in range(N)]
b_chk = [0 for _ in range(N)]
for i in range(N):
    if S[i] != T[i]:
        if S[i] == "A":
            a_chk[i] = 1
        else:
            b_chk[i] = 1

print(a_chk)
print(b_chk)

b_que = []
ans = 0
for i in range(N):
    if b_chk[i] == 1:
        b_que.append(i)
    elif b_que and a_chk[i] == 1:
        j = b_que.pop(0)
        b_chk[j] = 0
        a_chk[i] = 0
        ans += 1

print(a_chk)
print(b_chk)
print(ans)
print(b_que)

last_b_index = -1
for i in range(N-1, -1, -1):
    if T[i] == 'B':
        last_b_index = i
        break

first_a_index = -1
for i in range(N):
    if T[i] == "A":
        first_a_index = i
        break

for q in b_que:
    if q <= last_b_index:
        ans += 1
        b_chk[q] = 0


if 1 in b_chk:
    print(-1)
else:
    print(ans + sum(a_chk))
