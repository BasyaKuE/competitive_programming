N = int(input())
A = list(map(int, input().split()))
dic = {}
for i in range(3*N):
    if A[i] in dic:
        dic[A[i]].append(i+1)
    else:
        dic[A[i]] = [i+1]
#print(dic)
new_dic = {}
for k, v in dic.items():
    #print(k, v)
    new_dic[k] = v[1]
tmp = sorted(new_dic.items(), key=lambda x: x[1])
ans = []
for k, v in tmp:
    ans.append(k)
print(*ans)
