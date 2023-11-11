N, K = map(int, input().split())
med = []
S = 0
for i in range(N):
    a, b = map(int, input().split())
    S += b
    med.append([a, b])
sorted_med = sorted(med, key=lambda x: x[0])
# print(S, sorted_med)
if S <= K:
    print(1)
    exit()
for i in range(N):
    # print("i", i)
    S -= sorted_med[i][1]
    if S <= K:
        print(sorted_med[i][0]+1)
        exit()
"""
b_iの合計を足して
a_iの小さい順にそのb_iを引いて行く
"""
