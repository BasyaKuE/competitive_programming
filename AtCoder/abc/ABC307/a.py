N = int(input())
A = list(map(int, input().split()))
ans = []
chk = 0
for i in range(7*N):
    chk += A[i]
    if (i+1)%7==0:
        ans.append(chk)
        chk = 0
print(*ans)
