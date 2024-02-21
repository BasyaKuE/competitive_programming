import bisect
import itertools
import sys
from typing import List



def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)

N = int(input())
N -= 1
chk = str(int(base10int(N, 5)))
# print(chk)
ans = ""
for ch in chk:
    if ch == "0":
        ans += "0"
    elif ch == "1":
        ans += "2"
    elif ch == "2":
        ans += "4"
    elif ch == "3":
        ans += "6"
    elif ch == "4":
        ans += "8"
print(ans)
