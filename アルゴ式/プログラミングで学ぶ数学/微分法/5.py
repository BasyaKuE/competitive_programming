N = int(input())
A = list(map(int, input().split()))
B = [0 for _ in range(N)]
for i in range(N):
    B[i] = A[i+1]*(i+1)
print(*B)
