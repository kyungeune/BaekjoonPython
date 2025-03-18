import sys
sys.setrecursionlimit(1000)

def dfs(x, y):
    global num
    visited[x][y] = True
    num += 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and grid[nx][ny] == 1:
                dfs(nx,ny)

# 입력 받기
n = int(input())
grid = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

home = 0
cnt = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            num = 0 # 집 개수
            dfs(i, j)
            cnt.append(num)
            home += 1

print(home)
for i in sorted(cnt):
    print(i)