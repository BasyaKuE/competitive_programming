N = int(input())
A = list(map(str, input().split()))
A.sort()
x = 0
for a in A:
    x = (10*x + int(a)) % 998244353
print(x)
