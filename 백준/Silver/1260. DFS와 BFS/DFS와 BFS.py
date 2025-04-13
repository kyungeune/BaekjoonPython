

# DFS (Depth First Search)
# → 최대한 깊숙이 들어갔다가, 막히면 되돌아오는 방식
# → 스택(Stack) 구조처럼 작동하거나 재귀함수로 구현함

# BFS (Breadth First Search)
# → 가까운 곳부터 넓게 넓게 퍼져 나가는 방식
# → 큐(Queue)를 써서 구현함



# DFS
def dfs(graph, v, vDFS):
    vDFS[v] = True  # 방문 했다고 표시

    print(v, end=' ')

    for v in graph[v]:
        if not vDFS[v]:  # 방문 안 했으면
            dfs(graph, v, vDFS)


# BFS 함수
from collections import deque

def bfs(graph, v):
    vBFS = [False] * (len(graph))

    q = deque([v])

    vBFS[v] = True

    while q:
        v = q.popleft()
        print(v, end=' ')
        
        for v in graph[v]:
            if not vBFS[v]:
                vBFS[v] = True
                q.append(v)




n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


# 항상 작은 번호부터 방문할 수 있도록 보장
for i in graph:
    i.sort()



# DFS
vDFS = [False] * (n + 1)  # 방문여부
dfs(graph, v, vDFS)
print()

# BFS
bfs(graph, v)
