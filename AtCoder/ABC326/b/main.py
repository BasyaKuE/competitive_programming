N: int = int(input())
while True:
    N_str = str(N)
    if int(N_str[0])*int(N_str[1]) == int(N_str[2]):
        print(N_str)
        exit()
    N += 1
