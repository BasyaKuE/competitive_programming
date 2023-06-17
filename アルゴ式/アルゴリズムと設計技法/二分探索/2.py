# 解説AC
def chk(N, X):
    c = N+1
    for i in range(5):
        c = c*X + 1
    return c

N, M = map(int, input().split())
left = 0
right = 100
while (right-left>1e-4):
    mid = (right+left)/2
    c = chk(N, mid)
    if c < M:
        left = mid
    else:
        right = mid
print(left)

