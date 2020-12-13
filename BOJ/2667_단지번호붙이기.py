from collections import deque


def bfs(y, x):
    global home
    q = deque()
    q.append((y, x))
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < n and matrix[ny][nx] == 1:
                q.append((ny, nx))
                matrix[ny][nx] = 0
                home += 1


n = int(input())
matrix = [list(map(int, input())) for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 1:
            matrix[i][j] = 0
            home = 1
            bfs(i, j)
            result.append(home)


result.sort()
print(len(result))
for m in result:
    print(m)