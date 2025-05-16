from collections import deque
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]
    
    visited = [[False for i in range(m)] for j in range(n)]
    
    def BFS():
        q=deque()
        q.append((0,0))
        visited[0][0]=1
        
        while q:
            x,y = q.popleft()
            for i in range(4):
                nx = dx[i] + x
                ny = dy[i] + y
                
                if 0<=nx<n and 0<=ny<m:
                    if maps[nx][ny]==1 and visited[nx][ny]==False:
                        q.append((nx,ny))
                        visited[nx][ny] = visited[x][y] + 1
        
    BFS()
    if visited[n-1][m-1]==False:
        return -1
    else:
        return visited[n-1][m-1]