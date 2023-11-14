from typing import List

S: List[str] = input().strip()

# スタック
stack: List[str] = []
for ch in S:
    if len(stack) >= 2 and stack[-2] == "A" and stack[-1] == "B" and ch == "C":
        stack.pop()
        stack.pop()
    else:
        stack.append(ch)

result: str = "".join(stack)
print(result)
