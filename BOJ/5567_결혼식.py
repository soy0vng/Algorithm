import sys
from collections import deque


def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1
    while q:
        v = q.popleft()
        for i in friends[v]:
            if not visited[i]:
                visited[i] = visited[v] + 1
                q.append(i)


n = int(input())
m = int(input())
friends = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    friends[a].append(b)
    friends[b].append(a)

visited = [0] * (n+1)
cnt = 0
bfs(1)
for i in visited:
    if 1 < i <= 3:
        cnt += 1

print(cnt)