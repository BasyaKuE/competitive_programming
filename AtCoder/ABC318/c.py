N, D, P = map(int, input().split())
F = list(map(int, input().split()))
F.sort(reverse=True)
i = 0
ans = 0
for i in range(0, N, D):
    ans += min(sum(F[i:i+D]), P)
# print(i)
print(ans)
