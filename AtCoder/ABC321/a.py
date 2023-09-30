N = input()
for i in range(len(N)-1):
    if int(N[i]) > int(N[i+1]):
        continue
    else:
        print("No")
        exit()
print("Yes")
