from collections import deque

N, M = map(int, input().split())
G = [[] for _ in range(N)]
for _ in range(M):
    A, B = map(int, input().split())
    G[A-1].append(B)
    G[B-1].append(A)

que = deque()
rec = [False for _ in range(N)]
rec[0] = True
while que:
    i = que.popleft()
    for gi in G[i]:
        if rec[gi]:
            continue
        rec[gi] = True
        que.append(gi)