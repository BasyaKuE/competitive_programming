N = int(input())
A = list(map(int, input().split()))

G = [[] for _ in range(N+1)]
for i in range(1, N+1):
    G[i].append(A[i-1])

seen = [0] * (N+1)
cycle = []
stack = [1]

while stack:
    v = stack[-1]
    if seen[v]:
        # print("stack", stack)
        cycle = stack[stack.index(v):]
        break
    seen[v] = 1
    w = G[v][0]
    stack.append(w)

# print(len(cycle))
# print(*cycle)

M = len(cycle)-1
B = cycle[2:]
B.append(cycle[1])
print(M)
print(*B)
