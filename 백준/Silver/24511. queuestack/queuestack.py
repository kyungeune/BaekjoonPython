import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
which = list(map(int, input().split()))  # 큐냐 스택이냐
first = list(map(int, input().split()))  # 원소 초기값

m = int(input())
plus = list(map(int, input().split()))  # 넣어야 하는 원소들

q = deque()
ans = []

for i in range(n-1, -1, -1):  # 큐 초기화
    if which[i] == 0:
        q.append(first[i])

for i in plus:
    q.append(i)
    print(q.popleft(), end=' ')



# 풀이
# 스택은 무시하고 큐만 취급함
# ex) 기본 큐가 1 2 3 4 존재하고, 0을 넣어야 한다면 정답 방식으로는 list가
# 0 1 2 3이 되고, 4가 pop된다.
# 0을 왼쪽에 넣는 대신 입력을 거꾸로 받아서
# 4 3 2 1 0 으로 만든 후, popleft를 활용해 pop한다.