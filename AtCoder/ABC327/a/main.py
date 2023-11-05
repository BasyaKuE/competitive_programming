N: int = int(input())
S: str = input()

for i in range(N-1):
    if S[i] == "a" and S[i+1] == "b" or S[i] == "b" and S[i+1] == "a":
        print("Yes")
        exit()
print("No")
