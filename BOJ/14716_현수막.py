import sys
from collections import deque


def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx]:
                if matrix[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = 1


m, n = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]
visited = [[0]*n for _ in range(m)]
word = 0
dy = [-1, -1, 0, 1, 1, 1, 0, -1]
dx = [0, 1, 1, 1, 0, -1, -1, -1]
for i in range(m):
    for j in range(n):
        if matrix[i][j] and not visited[i][j]:
            bfs(i, j)
            word += 1

print(word)
