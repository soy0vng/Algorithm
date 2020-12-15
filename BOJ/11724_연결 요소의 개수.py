import sys
sys.setrecursionlimit(10000) # 최대 재귀 깊이 설정


def dfs(v):
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)


n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
visited = [0]*(n+1)
for i in range(1, n+1):
    if not visited[i]:
        dfs(i)
        cnt += 1
print(cnt)
