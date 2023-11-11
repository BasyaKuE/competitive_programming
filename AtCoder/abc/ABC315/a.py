S = input()
L = "a, e, i, o, u "
ans = ""
for ch in S:
    if ch in L:
        continue
    else:
        ans += ch
print(ans)
