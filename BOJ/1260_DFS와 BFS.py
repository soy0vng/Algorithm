from collections import deque


def dfs(v):
    visited[v] = 1
    print(v, end=" ")
    for i in range(1, n+1):
        if matrix[v][i] == 1 and not visited[i]:
            dfs(i)


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 0
    while q:
        v = q.popleft()
        print(v, end=" ")
        for i in range(1, n+1):
            if matrix[v][i] == 1 and visited[i]:
                q.append(i)
                visited[i] = 0


n, m, v = map(int, input().split())
matrix = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1
visited = [0] * (n+1) # 정점 방문 여부 확인
dfs(v)
print()
bfs(v)