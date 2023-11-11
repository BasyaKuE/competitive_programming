from bisect import bisect_right

N, M, P = map(int, input().split())
A = sorted(list(map(int, input().split())))
B = sorted(list(map(int, input().split())))
B_cumsum = [0] * (M + 1)
for i in range(M):
    B_cumsum[i+1] = B_cumsum[i] + B[i]

total = 0
for a in A:
    index = bisect_right(B, P - a)
    total += (P * (M - index) + B_cumsum[index] + a * index)

print(total)
