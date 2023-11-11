N = int(input())
S = input()
a_c, b_c, c_c = 0, 0, 0
for i in range(N):
    s = S[i]
    if s == "A":
        a_c += 1
    elif s == "B":
        b_c += 1
    else:
        c_c += 1
    if a_c >= 1 and b_c >= 1 and c_c >= 1:
        print(i+1)
        exit()
