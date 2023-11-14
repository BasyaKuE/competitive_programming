import bisect
import itertools
import sys
from typing import List

class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        self.diff_weight = [0] * n

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            y = self.find(self.parent[x])
            self.diff_weight[x] += self.diff_weight[self.parent[x]]
            self.parent[x] = y
            return y

    def unite(self, x, y, w):
        w += self.weight(x) - self.weight(y)
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.rank[x] < self.rank[y]:
            x, y = y, x
            w = -w
        if self.rank[x] == self.rank[y]:
            self.rank[x] += 1
        self.parent[y] = x
        self.diff_weight[y] = w
        return True

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def weight(self, x):
        self.find(x)
        return self.diff_weight[x]

    def diff(self, x, y):
        return self.weight(y) - self.weight(x)


N, Q = map(int, input().split())
uf = UnionFind(N)
good_set = []

for i in range(1, Q + 1):
    a, b, d = map(int, input().split())
    a -= 1
    b -= 1
    if uf.same(a, b):
        if uf.diff(a, b) != d:
            continue
    else:
        uf.unite(a, b, d)
    good_set.append(i)

print(*good_set)
