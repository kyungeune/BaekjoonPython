import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for _ in range(n):
    ans = input().split()
    
    if ans[0] == 'push':
        x = ans[1]
        q.append(x)
    elif ans[0] == 'pop':
        print(q.popleft() if len(q)!=0 else '-1')
    elif ans[0] == 'size':
        print(len(q))
    elif ans[0] == 'empty':
        print('1' if len(q)==0 else '0')
    elif ans[0] == 'front':
        print(q[0] if len(q)!=0 else '-1')
    elif ans[0] == 'back':
        print(q[-1] if len(q)!=0 else '-1')
    
