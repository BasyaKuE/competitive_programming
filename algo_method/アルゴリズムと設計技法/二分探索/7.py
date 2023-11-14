N = int(input())
X = list(map(int, input().split()))
for i in range(N):
    left = 0
    right = 10**18
    while left != right:
        mid = (left+right)//2
        chk = (mid+1)*mid//2
        if chk < X[i]:
            left = mid+1
        else:
            right = mid
        #print("mid", mid)
    print(left)

