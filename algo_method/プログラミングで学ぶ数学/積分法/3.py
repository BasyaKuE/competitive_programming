def func(x):
    A = (b-a)/h
    B = a
    return A*x + B


a, b, h = map(int, input().split())
for k in range(6):
    ans = 0
    n = 10**k
    for i in range(n):
        # print("func", func(i))
        ans += func((h/n)*i) * h/n
    print(ans)
