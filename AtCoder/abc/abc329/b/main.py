N = int(input())
A = list(map(int, input().split()))
chk = sorted(set(A))
print(chk[-2])