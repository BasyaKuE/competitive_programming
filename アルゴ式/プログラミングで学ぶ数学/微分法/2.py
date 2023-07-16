N, a, b = map(int, input().split())
for i in range(N):
    x_i = (b*b-a*a)/(b-a)
    print(x_i)
    b = (a+b)/2
