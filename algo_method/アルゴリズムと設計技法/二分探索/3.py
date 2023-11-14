from bisect import bisect_left
N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
for i in range(M):
    b = B[i]
    ans = bisect_left(A, b)
    print(ans)
