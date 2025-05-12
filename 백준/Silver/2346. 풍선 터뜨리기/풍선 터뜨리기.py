import sys
from collections import deque

input = sys.stdin.readline
q = deque()
n = int(input())

a = list(input().split())
for i in range(n):
    x = str(a[i]) + " " + str(i+1)  # ['3 1', '2 2', '1 3', '-3 4', '-1 5']
    q.append(x)


k = q.popleft()
print(k.split()[1], end=' ')
while q:
    x = int(k.split()[0])
    if x>0:
        for _ in range(x-1):
            imsi = q.popleft()
            q.append(imsi)
    elif x<0:
        for _ in range(-x):
            imsi = q.pop()
            q.appendleft(imsi)
    if q:
        k = q.popleft()
        print(k.split()[1], end=' ')
    else:
        break
