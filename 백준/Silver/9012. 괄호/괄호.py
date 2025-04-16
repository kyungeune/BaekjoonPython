import sys
from collections import deque
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    q = deque(input().strip())
    cnt = 0
    imsi = 1

    while q:
        fir = q.popleft()
        if fir == '(':
            cnt+=1
        else:
            cnt-=1
            if cnt<0:
                imsi=0
                break
        
    if cnt!=0:
        imsi=0

    if imsi == 1:
        print('YES')
    else:
        print('NO')