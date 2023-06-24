N = int(input())
S = [input() for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            continue
        chk = S[i]+S[j]
        if chk == chk[::-1]:
            print("Yes")
            exit()
print("No")
