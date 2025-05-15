import sys
input = sys.stdin.readline

def DFS(idx):
    global graph, visited, ans
    #print(idx, end=' ')
    ans+=1
    visited[idx]=1
    for i in range(n+1):
        if graph[idx][i]==1 and visited[i]==0:
            DFS(i)
    

n=int(input())
m=int(input())
graph=[[0]*(n+1) for _ in range(n+1)]
visited=[0]*(n+1)
ans=-1

for i in range(m):
    a,b=map(int, input().split())
    graph[b][a]=1
    graph[a][b]=1

DFS(1)
print(ans)