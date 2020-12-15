from collections import deque


def bfs(y, x):
    q = deque()
    q.append((y, x))

    while q:
        y, x = q.popleft()
        for d in range(8):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < h and 0 <= nx < w and matrix[ny][nx] == 1:
                q.append((ny, nx))
                matrix[ny][nx] = 0


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    matrix = [list(map(int, input().split())) for _ in range(h)]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == 1:
                bfs(i, j)
                cnt += 1

    print(cnt)