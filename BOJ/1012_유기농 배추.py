from collections import deque


def bfs(y, x):
    q = deque()
    q.append((y, x))
    dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < m and area[ny][nx] == 1:
                area[ny][nx] = 0
                q.append((ny, nx))


for tc in range(1, int(input())+1):
    m, n, k = map(int, input().split())
    area = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        area[b][a] = 1

    result = 0
    for i in range(n):
        for j in range(m):
            if area[i][j] == 1:
                bfs(i, j)
                area[i][j] = 0
                result += 1

    print(result)