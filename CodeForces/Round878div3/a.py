t = int(input())
for i in range(t):
    n = int(input())
    a = input()
    ans = ""
    first = ""
    for j in range(n):
        if first == "":
            first = a[j]
            ans += a[j]
        elif first == a[j]:
            first = ""
    print(ans)
