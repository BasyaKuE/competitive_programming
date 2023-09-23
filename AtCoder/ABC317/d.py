N = int(input())
Y_upper = []
Z_sum = 0
X_z_sum = 0
for _ in range(N):
    X, Y, Z = map(int, input().split())
    if X > Y:
        X_z_sum += Z
    else:
        Y_upper.append((X, Y, Z, Y-X))
    Z_sum += Z
if X_z_sum > Z_sum//2:
    print(0)
else:
    ans = 0
    Y_upper.sort(key=lambda x: (-x[2]*x[3], -x[3]))
    for info in Y_upper:
        X, Y, Z, div = info
        # print(X, Y, Z, div)
        ans += (Y-X)//2 + 1
        X_z_sum += Z
        if X_z_sum > Z_sum//2:
            print(ans)
            exit()
