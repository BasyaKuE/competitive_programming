N = int(input())
A = list(map(int, input().split()))
chk = A[0]
for i in range(N):
    if chk != A[i]:
        print("No")
        exit()
print("Yes")
