a, b = map(int, input().split())
if a < b:
    print(b/(b-a))
else:
    print(-1)
