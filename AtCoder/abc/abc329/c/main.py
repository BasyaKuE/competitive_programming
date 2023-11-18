from collections import defaultdict
N = int(input())
S = input()
now_ch = None
# 各文字種類の最大の長さを調べる
chk = defaultdict(int)
l = 0
for ch in S:
    if ch == now_ch:
        l += 1
    else:
        if now_ch == None:
            pass
        else:
            chk[now_ch] = max(l, chk[now_ch])
        l = 1
        now_ch = ch
chk[now_ch] = max(l, chk[now_ch])
ans = 0
for k, v in chk.items():
    ans += v
print(ans)