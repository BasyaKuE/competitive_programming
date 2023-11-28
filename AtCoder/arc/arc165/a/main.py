T: int = int(input())
for _ in range(T):
    N: int = int(input())
    chk: int = 0
    for i in range(1, 1000000000 // 2):
        chk += i
        if chk == N:
            print("Yes")
            break
        elif chk > N:
            print("No")
            break
