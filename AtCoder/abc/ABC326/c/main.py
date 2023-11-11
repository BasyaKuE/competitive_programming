import bisect
N, M = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
# print(*A)
ans = 0
for i in range(N):
    # chk = bisect.bisect_right(A, A[i]+M)
    # print("i", i, "chk", chk)
    ans = max(ans, bisect.bisect_right(A, A[i]+M-1)-i)
print(ans)
