S = list(map(int, input().split()))
for i in range(8):
    if i == 0:
        if S[i] % 25 != 0 or S[i] < 100 or 675 < S[i]:
            print("No")
            exit()
    else:
        if S[i] % 25 != 0 or S[i] < S[i-1] or S[i] < 100 or 675 < S[i]:
            print("No")
            exit()
print("Yes")
