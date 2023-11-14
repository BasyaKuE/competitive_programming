def func(a, b, x):
    return a*x + b


L, R, a, b = map(int, input().split())
ans = 0
for i in range(L, R):
    ans += func(a, b, i)
print(ans)
