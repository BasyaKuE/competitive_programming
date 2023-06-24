def solve(S):
    stack = []
    result = []

    for ch in S:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack:
                stack.pop()
            else:
                result.append(ch)
        else:
            if not stack:
                result.append(ch)
            else:
                stack[-1] += ch
        #print(ch, result, stack)
    result = result + stack
    return ''.join(result)

N = int(input())
S = input()
print(solve(S))
