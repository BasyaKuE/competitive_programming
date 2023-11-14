# 解説AC
N, K = map(int, input().split())
A = list(map(int, input().split()))
A.sort()
ans = 0
for i in range(N):
    a = A[i]
    left = 0
    right = N
    while left != right:
        mid = (left+right)//2
        if A[mid] < K-a: #怪しい
            left = mid+1 #怪しい
        else:
            right = mid
    ans += N-left
print(ans)
