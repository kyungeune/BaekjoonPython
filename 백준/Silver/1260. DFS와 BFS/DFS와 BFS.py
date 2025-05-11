import sys
def dfs(idx) : 
    global visited
    visited[idx] = True  # 다시는 들어오지 마라
    print(idx, end = ' ')
    for next in range(1, N+1):
        if not visited[next] and graph[idx][next]:  # next가 방문되지 않았다 and 갈 수 있는 곳이라면
            dfs(next)

def bfs():
    global q, visited
    while q:
        cur = q.pop(0)
        print(cur, end=' ')
        for next in range(1, N+1):
            if not visited[next] and graph[cur][next]:
                visited[next] = True
                q.append(next)

# 0. 입력 및 초기화
# 변수 설명
# N: 정점의 개수
# M: 간선의 개수
# V: 탐색을 시작할 정점의 번호
input = sys.stdin.readline
N, M, V = map(int, input().split())

graph = [[False]*(N+1) for _ in range(N+1)]  # 정점의 개수로(0~N) 구성된 2차원 배열
visited = [False] * (N+1)

# 1. graph 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

# 2. DFS(깊이 우선 탐색)
dfs(V)
print()

# 3. BFS(너비 우선 탐색)
visited = [False]*(N+1)
q=[V]  # 
visited[V]=True
bfs()