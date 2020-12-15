import sys
from collections import deque


def bfs(y, x):
    global answer
    q = deque()
    q.append((y, x))
    while q:
        y, x = q.popleft()
        for d in range(4):
            ny = y + dy[d]
            nx = x + dx[d]
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                if painting[ny][nx] == painting[y][x]:
                    q.append((ny, nx))
                    visited[ny][nx] = 1


n = int(input())
painting = [list(sys.stdin.readline().rstrip()) for _ in range(n)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# 적록색약 X
visited = [[0]*n for _ in range(n)]
answer = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            answer += 1
print(answer, end=" ")

# 적록색약 O
for i in range(n):
    for j in range(n):
        if painting[i][j] == 'R':
            painting[i][j] = 'G'

visited = [[0]*n for _ in range(n)]
answer2 = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            bfs(i, j)
            answer2 += 1
print(answer2)


