import bisect
import itertools
import sys
from typing import List

H, W, N = map(int, input().split())
G = [["." for _ in range(W)] for _ in range(H)]

di = "up"
x, y = 0, 0
for i in range(N):
    # print("now", x, y)
    if G[y][x] == ".":
        G[y][x] = "#"
        if di == "up":
            di = "right"
        elif di == "right":
            di = "down"
        elif di == "down":
            di = "left"
        else:
            di = "up"
    else:
        G[y][x] = "."
        if di == "up":
            di = "left"
        elif di == "right":
            di = "up"
        elif di == "down":
            di = "right"
        else:
            di = "down"
    if di == "up":
        y -= 1
        if y < 0:
            y = H-1
    elif di == "right":
        x += 1
        if x >= W:
            x = 0
    elif di == "down":
        y += 1
        if y >= H:
            y = 0
    else:
        x -= 1
        if x < 0:
            x = W-1
for row in G:
    ans = "".join(row)
    print(ans)
