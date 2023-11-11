import sys
from collections import deque, defaultdict

sys.setrecursionlimit(10**6)

def topo_sort(graph, n):
    in_degree = [0] * (n+1)
    for i in range(1, n+1):
        for j in graph[i]:
            in_degree[j] += 1

    queue = deque()
    for i in range(1, n+1):
        if in_degree[i] == 0:
            queue.append(i)

    order = []
    while queue:
        v = queue.popleft()
        order.append(v)
        for u in graph[v]:
            in_degree[u] -= 1
            if in_degree[u] == 0:
                queue.append(u)
    return order

N = int(input().strip())
graph = defaultdict(list)
for i in range(1, N+1):
    data = list(map(int, input().split()))
    for j in data[1:]:
        graph[i].append(j)

order = topo_sort(graph, N)

res = []
visited = set()
def dfs(v):
    if v in visited:
        return
    visited.add(v)
    for u in graph[v]:
        dfs(u)
    if v != 1:
        res.append(v)

dfs(1)

print(" ".join(map(str, reversed(res))))
