N = int(input())
W = list(map(int, input().split()))
C = sorted(W)
for k in range(N):
    w = W[k]
    left = 0
    right = N-1
    while right!=left:
        mid = (right+left)//2
        if C[mid] >= w:
            right = mid
        else:
            left = mid+1
    print(left)
