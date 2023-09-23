N, M = map(int, input().split())
S = input()
C = list(map(int, input().split()))
memo = [[] for _ in range(M)]
for i in range(1, M+1):
    swap_ch = []
    for c in C:
        if c == i:
            swap_ch.append([S[i-1], i])

