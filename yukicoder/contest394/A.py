que = 50
while True:
    print("?", que)
    res = int(input())
    if res < que:
        que = res
    elif res > que:
        pass
    else:
        print("!", )
