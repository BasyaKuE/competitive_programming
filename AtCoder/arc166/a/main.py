T: int = int(input())
for _ in range(T):
    N_str, X, Y = map(str, input().split())
    N: int = int(N_str)
    if X == Y:
        print("Yes")
        continue
    # まずCがない場合
    for i in range(N-1):
        if X[i] == "A" and X[i+1] == "B" and not (Y[i] == "A" and Y[i+1] == "B"):
            X = X[:i] + "BA" + X[i+1:]
