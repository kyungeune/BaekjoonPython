import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()

for i in range(1, n+1):  # 넣기
    q.append(i)

while len(q)!=1:
    q.popleft()  # 맨 위 꺼내기
    x = q.popleft()  # 맨 위에있는거 꺼내서
    q.append(x)  # 맨 밑으로

print(q[0])