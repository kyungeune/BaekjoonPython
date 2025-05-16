from collections import deque

def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    visited=[[False for i in range(m)] for j in range(n)]
    
    dx=[1,-1,0,0]
    dy=[0,0,1,-1]
    
    def BFS(x, y):
        q = deque()
        q.append((x,y))
        visited[x][y]=1
        
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]
                
                if 0<=nx<n and 0<=ny<m:
                    if visited[nx][ny]==False and maps[nx][ny]==1:
                        visited[nx][ny] = visited[x][y] + 1
                        q.append((nx,ny))
    
    BFS(0,0)
    if visited[n-1][m-1] == False:
        return -1
    return visited[n-1][m-1]