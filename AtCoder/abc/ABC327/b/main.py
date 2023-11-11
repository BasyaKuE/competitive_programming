B: int = int(input())
for A in range(1, 1000):
    if A**A == B:
        print(A)
        exit()
print(-1)
