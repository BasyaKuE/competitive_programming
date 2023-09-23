N = int(input())
C_list, A_list = [], []
for _ in range(N):
    C = int(input())
    A = list(map(int, input().split()))
    C_list.append(C)
    A_list.append(A)
X = int(input())
ans_list = []
min_C = float("inf")
for i in range(N):
    C = C_list[i]
    A = A_list[i]
    if X in A and min_C > C:
        min_C = C
for i in range(N):
    C = C_list[i]
    A = A_list[i]
    if X in A and C == min_C:
        ans_list.append([i+1, C])
print(len(ans_list))
ans = []
for l in ans_list:
    ans.append(l[0])
print(*sorted(ans))
