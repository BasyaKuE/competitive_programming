import bisect
from collections import deque
from operator import itemgetter

n,m = map(int,input().split())
noodle = [list(map(int,input().split())) for _ in range(m)]
noodle.append([10**10, 0]) # add sach time outlet
noodle.sort(key=itemgetter(0))

alist=[0]*(n+1)
nlist=deque([(0,0)]*n)
noodle=deque(noodle)

while noodle:
    x,y,z=noodle.popleft() # time to frow noodle

    if nlist[0][1]<=x: # if the man can reach for noodle
        a,b=nlist.popleft()
        alist[a+1]+=y
        bisect.insort_right(nlist,((a+1),b+z+x))

    else:noodle.appendleft((x,y,z))

for i in range(1,n+1):print(alist[i])
