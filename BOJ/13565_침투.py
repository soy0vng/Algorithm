import sys
from collections import deque


def bfs(y, x):
    global result
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        if y == m - 1:
            result = 'YES'
            return
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx]:
                if matrix[ny][nx] == 0:
                    q.append((ny, nx))
                    visited[ny][nx] = 1


m, n = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
result = 'NO'
for i in range(n):
    if matrix[0][i] == 0 and not visited[0][i]:
        visited[0][i] = 1
        bfs(0, i)

print(result)