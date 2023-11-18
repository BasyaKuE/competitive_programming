import collections

N, M = map(int, input().split())
A = list(map(int, input().split()))

v = collections.defaultdict(int)

now_win = 0
max_v = 0

for i in range(M):
    c = A[i]
    v[c] += 1
    
    if v[c] > max_v or (v[c] == max_v and c < now_win):
        now_win = c
        max_v = v[c]

    # print(v)
    print(now_win)