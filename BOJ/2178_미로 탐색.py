from collections import deque


def bfs(y, x):
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and maze[ny][nx] == 1:
                maze[ny][nx] = maze[y][x] + 1
                q.append((ny, nx))
    return maze[n-1][m-1]


n, m = map(int, input().split())
maze = [list(map(int, input())) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
print(bfs(0, 0))