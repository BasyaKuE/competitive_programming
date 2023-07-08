def tate(i, ch, G):
    if G[0][i] == ch and G[1][i] == ch and G[2][i] == ch:
        return True
    else:
        return False


def naname(ch, G):
    if G[0][0] == ch and G[1][1] == ch and G[2][2] == ch:
        return True
    elif G[0][2] == ch and G[1][1] == ch and G[2][0] == ch:
        return True
    else:
        False


t = int(input())
for _ in range(t):
    G = [input() for __ in range(3)]
    if "XXX" in G:
        print("X")
    elif "OOO" in G:
        print("O")
    elif "+++" in G:
        print("+")
    else:
        ans = ""
        for i in range(3):
            if tate(i, "X", G):
                ans = "X"
                break
            elif naname("X", G):
                ans = "X"
                break
            elif tate(i, "O", G):
                ans = "O"
                break
            elif naname("O", G):
                ans = "O"
                break
            elif tate(i, "+", G):
                ans = "+"
            elif naname("+", G):
                ans = "+"
        if ans == "":
            print("DRAW")
        else:
            print(ans)
