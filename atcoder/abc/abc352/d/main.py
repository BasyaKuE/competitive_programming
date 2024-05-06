from sortedcontainers import SortedSet

N, K = map(int, input().split())
P = list(map(int, input().split()))
for i in range(N):
    P[i] -= 1
Q = [0 for _ in range(N)]
for i in range(N):
    Q[P[i]] = i
S = SortedSet()
ans = N
for i in range(N):
    S.add(Q[i])
    if len(S) > K:
        S.remove(Q[i-K])
    if len(S) == K:
        ans = min(ans, S[-1]-S[0])
print(ans)
