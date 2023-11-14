N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    q = list(map(int, input().split()))
    if q[0] == 0:
        A.insert(q[1], q[2])
    elif q[0] == 1:
        A.pop(q[1])
    else:
        print(A.count(q[1]))
    # print(A)
