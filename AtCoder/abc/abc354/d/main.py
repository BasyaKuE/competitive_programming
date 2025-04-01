import bisect
import itertools
import sys
import collections

A, B, C, D = map(int, input().split())
W = C - A - (A%4)
H = D - B - (B%4)
a = A%4
b = B%4

w = W//4
w_a = W%4
h = H//4
h_a = H%4
ans = w*h*16
print(ans, w_a, h_a)

if h_a == 0:
    if w_a == 0:
        ans += 0
    elif w_a == 1:
        ans += 3
    elif w_a == 2:
        ans += 6
    else:
        ans += 7
elif h_a == 1:
    if w_a == 0:
        ans += 4
    elif w_a == 1:
        ans += 2
    elif w_a == 2:
        ans += 3
    else:
        ans += 3
elif h_a == 2:
    if w_a == 0:
        ans += 8
    elif w_a == 1:
        ans += 3
    elif w_a == 2:
        ans += 6
    else:
        ans += 7
else:
    if w_a == 0:
        ans += 4 + 8
    elif w_a == 1:
        ans += 2 + 3
    elif w_a == 2:
        ans += 3 + 6
    else:
        ans += 3 + 7

if a == 0:
    if b == 0:
        ans += 0
    elif b == 1:
        if w_a == 0:
            ans += 4
        elif w_a == 1:
            ans += 2
        elif w_a == 2:
            ans += 3
        else:
            ans += 3
    elif b == 2:
        if w_a == 0:
            ans += 8
        elif w_a == 1:
            ans += 3
        elif w_a == 2:
            ans += 6
        else:
            ans += 7
    else:
        if w_a == 0:
            ans += 4 + 8
        elif w_a == 1:
            ans += 2 + 3
        elif w_a == 2:
            ans += 3 + 6
        else:
            ans += 3 + 7
elif a == 1:
    if b == 0:
        

print(ans)
