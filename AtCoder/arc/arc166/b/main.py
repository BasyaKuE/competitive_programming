N, a, b, c = map(int, input().split())
A = list(map(int, input().split()))

distances = [min(a % x, b % x, c % x) if x != 0 else min(a, b, c) for x in A]
print(sum(distances))
