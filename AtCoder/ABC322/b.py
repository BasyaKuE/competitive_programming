N, M = map(int, input().split())
S = input()
T = input()
if T[0:len(S)] == S and T[-len(S):] == S:
    print(0)
elif T[0:len(S)] == S:
    print(1)
elif T[-len(S):] == S:
    print(2)
else:
    print(3)
