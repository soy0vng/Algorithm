# from collections import deque


# 1
def dfs(v):
    global result
    visited[v] = 1
    for i in range(1, n+1):
        if matrix[v][i] == 1 and not visited[i]:
            dfs(i)
            result += 1
    return result


# 2
# def bfs(v):
#     global result
#     q = deque()
#     q.append(v)
#     visited[v] = 1
#     while q:
#         v = q.popleft()
#         for i in range(1, n+1):
#             if matrix[v][i] == 1 and not visited[i]:
#                 q.append(i)
#                 visited[i] = 1
#                 result += 1
#     return result


n = int(input())
connect = int(input())
matrix = [[0]*(n+1) for _ in range(n+1)]
for _ in range(connect):
    a, b = map(int, input().split())
    matrix[a][b] = matrix[b][a] = 1

visited = [0]*(n+1)
result = 0
print(dfs(1))
# print(bfs(1))