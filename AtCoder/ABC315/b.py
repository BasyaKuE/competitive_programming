M = int(input())
D = list(map(int, input().split()))
mid = sum(D)//2 + 1
s = 0
for i in range(M):
    chk = s + D[i]
    if chk >= mid:
        print(i+1, mid-s)
        exit()
    s = chk
