from bisect import bisect_left
N = int(input())
W = list(map(int, input().split()))
C = sorted(W)
for i in range(N):
    ans = bisect_left(C, W[i])
    print(ans)
