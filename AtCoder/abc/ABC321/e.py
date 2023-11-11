T = int(input())
for _ in range(T):
    N, X, K = map(int, input().split())
    v = X
    for _ in range(K):
        v >>= 1
    answer = 0
    while v <= N:
        answer += 1
        v <<= 1
    print(answer)
