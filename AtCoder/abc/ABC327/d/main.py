import sys
from typing import List

sys.setrecursionlimit(100000000)

N, M = map(int, input().split())
A: List[int] = list(map(int, input().split()))
B: List[int] = list(map(int, input().split()))

G: List[List[int]] = [[] for _ in range(N)]
for i in range(M):
    G[A[i]-1].append(B[i]-1)
    G[B[i]-1].append(A[i]-1)

# ここからDFS
X: List[int] = [-1 for _ in range(N)]
bipartite: bool = True


def dfs(c: int, x: int) -> None:
    global bipartite
    X[c] = x
    for d in G[c]:
        if X[d] == -1:
            dfs(d, 1-x)
        elif X[d] == X[c]:
            bipartite = False


for i in range(N):
    if X[i] == -1:
        dfs(i, 0)

if bipartite:
    print("Yes")
else:
    print("No")
