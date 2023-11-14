import bisect
import itertools
import sys
from typing import List

N, M, K = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(M)]

minimum_cost = K

# Union-Find
for comb in itertools.combinations(edges, N - 1):
    # print(comb)
    parent = list(range(N + 1))

    def find(x):
        if parent[x] == x:
            return x
        parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        px = find(x)
        py = find(y)
        if px != py:
            parent[px] = py

    cost = 0
    for u, v, w in comb:
        if find(u) != find(v):
            union(u, v)
            cost += w

    if len(set(find(i) for i in range(1, N + 1))) == 1:
        minimum_cost = min(minimum_cost, cost % K)

print(minimum_cost)
