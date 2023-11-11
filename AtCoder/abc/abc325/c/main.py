from collections import deque
from typing import List, Tuple, Deque

H, W = map(int, input().split())
S: List[str] = [input() for _ in range(H)]
ans: int = 0
adjacents: List[Tuple[int]] = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (1, 1), (1, -1), (-1, -1)]
rec: List[List[bool]] = [[False for _ in range(W)] for __ in range(H)]

for i in range(H):
    for j in range(W):
        if rec[i][j]:
            continue
        rec[i][j] = True
        if S[i][j] == ".":
            continue
        ans += 1
        que: Deque[List[int]] = deque([[i, j]])
        while que:
            di, dj = que.popleft()
            for dx, dy in adjacents:
                if 0 <= di+dx < H and 0 <= dj+dy < W:
                    if rec[di+dx][dj+dy]:
                        continue
                    rec[di+dx][dj+dy] = True
                    if S[di+dx][dj+dy] == "#":
                        que.append([di+dx, dj+dy])
print(ans)