import sys
from collections import deque
input = sys.stdin.readline
t = int(input())

dx = [0,0,-1,1]
dy = [1,-1,0,0]

def bfs(x, y, graph, n, m):
    queue = deque()
    queue.append((x, y))
    graph[y][x] = 0  # 방문 처리
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):  # 상하좌우 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위 확인 + 방문할 수 있는 곳인지 확인
            if 0 <= nx < m and 0 <= ny < n and graph[ny][nx] == 1:
                graph[ny][nx] = 0
                queue.append((nx, ny))



for _ in range(t):
    rslt = 0
    m,n,k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1  # 주의

    for j in range(n):
        for z in range(m):
            if graph[j][z] == 1:
                bfs(z,j,graph,n,m)
                rslt+=1

    print(rslt)