import collections

N, Q = map(int, input().split())
C = list(map(int, input().split()))

box = collections.defaultdict(set)

for i, c in enumerate(C, 1):
    box[i].add(c)

for _ in range(Q):
    a, b = map(int, input().split())
    box[b].update(box[a])
    box[a].clear()

    print(len(box[b]))

