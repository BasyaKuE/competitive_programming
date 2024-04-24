import bisect
import itertools
import sys
from typing import List

S = input()
for i in range(len(S)):
    if i == 0 and S[i] != S[i].upper():
        print("No")
        exit()
    elif i != 0 and S[i] != S[i].lower():
        print("No")
        exit()
print("Yes")
