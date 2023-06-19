N, M = map(int, input().split())
W = list(map(int, input().split()))
dp = [0 for _ in range(2**N)]
for i in range(N):
    
