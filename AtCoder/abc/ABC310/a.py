N, P, Q = map(int, input().split())
D = list(map(int, input().split()))
d = min(D)
print(min(P, d+Q))
