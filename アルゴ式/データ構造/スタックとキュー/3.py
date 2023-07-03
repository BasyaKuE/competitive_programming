N, Q = map(int, input().split())
A = [-1 for _ in range(N)]
head, tail = 0, N-1
for _ in range(Q):
    q = list(map(int, input().split()))
    if len(q) == 1:
        for __ in range(q[0]):
            A[head] = -1
            head += 1
    else:
        v = q[1]
        A[tail] = v
        tail += 1
for a in A:
    print(a)
