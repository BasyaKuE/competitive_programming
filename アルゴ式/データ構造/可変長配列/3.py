N = int(input())
A = list(map(int, input().split()))
Q = int(input())
for _ in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 0:
        A.append(query[1])
    else:
        if len(A) == 0:
            print("Error")
        else:
            print(A.pop())
