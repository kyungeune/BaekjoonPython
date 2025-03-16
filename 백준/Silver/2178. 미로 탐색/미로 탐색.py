# 최단 경로 문제 --> BFS 코드 사용
from collections import deque
import sys


def bfs(maze, n, m):
    dx = [-1, 1, 0, 0] # x축(세로 방향): 위(-1), 아래(+1)
    dy = [0, 0, -1, 1] # y축(가로 방향): 왼쪽(-1), 오른쪽(+1)
    
    q = deque([(0, 0)])

    while q: # q가 빌 때까지 반복
        x, y = q.popleft() # 큐에서 현재 위치 꺼내기

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i] # 상, 하, 좌, 우로 이동할 좌표 계산

            if nx<0 or ny<0 or nx>=n or ny>=m:
                continue
            
            if maze[nx][ny] == 1: # 이동할 수 있는 칸(1)이라면
                maze[nx][ny] = maze[x][y] + 1 # 이동 거리 기록(누적)
                q.append((nx, ny)) # 다음 탐색할 위치 큐에 추가

    return maze[n-1][m-1]
    

# n, m = input().split()
# n = int(n)
# m = int(m)
n, m = map(int, input().split())

maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]  # 미로 입력

print(bfs(maze, n, m))