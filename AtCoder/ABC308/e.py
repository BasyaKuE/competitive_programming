N = int(input())
A = list(map(int, input().split()))
S = input()
D = {"M":[], "E":[], "X":[]}
for i in range(N):
    s = S[i]
    D[s].append(i)

