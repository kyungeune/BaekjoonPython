from collections import deque
def solution(maps):
    n=len(maps)
    m=len(maps[0])
    visited=[[False for i in range(len(maps[0]))] for j in range(len(maps))]
    
    
    dx = [-1,1,0,0]
    dy = [0,0,1,-1]

    def BFS(x,y):
        q=deque()
        q.append((x,y))
        visited[x][y]=True
        
        while q:
            x,y = q.popleft()
            
            for i in range(4):
                nx = x+dx[i]
                ny = y+dy[i]

                if nx<0 or nx>=n or ny<0 or ny>=m:
                    continue
                if maps[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny]=True
                    maps[nx][ny] = maps[x][y] + 1
                    q.append((nx,ny))

        if visited[n-1][m-1]==False:
            return -1
        else:
            return maps[n-1][m-1]
        
    return BFS(0,0)