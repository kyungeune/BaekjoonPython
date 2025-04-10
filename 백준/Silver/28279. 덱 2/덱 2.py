from collections import deque
import sys
input = sys.stdin.readline

q = deque()
n = int(input())

for _ in range(n):
    x = input().split()

    if x[0] == '1':
        q.appendleft(int(x[1]))
    elif x[0] == '2':
        q.append(int(x[1]))
    elif x[0] == '3':
        if not q: print('-1')
        else: print(q.popleft())
    elif x[0] == '4':
        if not q: print('-1')
        else: print(q.pop())
    elif x[0] == '5':
        print(len(q))
    elif x[0] == '6':
        if not q: print('1')
        else: print('0')
    elif x[0] == '7':
        if not q: print('-1')
        else: print(q[0])
    elif x[0] == '8':
        if not q: print('-1')
        else: print(q[len(q)-1])