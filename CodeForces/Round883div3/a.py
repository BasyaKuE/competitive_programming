ｘt = int(input())
for _ in range(t):
    n = int(input())
    ans = 0
    for i in range(n):
        a, b = map(int, input().split())
        if a > b:
            ans += 1
    print(ans)
