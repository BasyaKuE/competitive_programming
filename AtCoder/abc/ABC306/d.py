N = int(input())
dishes = [list(map(int, input().split())) for _ in range(N)]
DP = [[0 if j == 0 else -1 for j in range(2)] for _ in range(N)]
X, Y = dishes[0][0], dishes[0][1]
if X == 0:
    DP[0][0] = max(Y, 0)
    DP[0][1] = -1
else:
    DP[0][0] = 0
    DP[0][1] = Y
for i in range(1, N):
    X, Y = dishes[i][0], dishes[i][1]
    if X == 0:
        if DP[i-1][1] != -1:
            DP[i][0] = max([DP[i-1][0], DP[i-1][1] + Y, DP[i-1][0]+Y])
            DP[i][1] = DP[i-1][1]
        else:
            DP[i][0] = max([DP[i-1][0], DP[i-1][0]+Y])
            DP[i][1] = DP[i-1][1]
        #print("X0",DP[i][0], DP[i][1])
    else:
        if DP[i-1][1] != -1:
            DP[i][0] = DP[i-1][0]
            DP[i][1] = max(DP[i-1][0] + Y, DP[i-1][1])
        else:
            DP[i][0] = DP[i-1][0]
            DP[i][1] = DP[i-1][0] + Y
        #print("X1",DP[i][0], DP[i][1])
ans = -1
#print(DP)
for i in range(N):
    ans = max(ans, max(DP[i]))
print(max(ans, 0))
