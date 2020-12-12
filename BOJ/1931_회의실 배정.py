n = int(input())
meetings = [list(map(int, input().split())) for _ in range(n)]
# 회의가 빨리 끝나는 순으로 정렬 + 끝나는 시간이 같은 경우 빨리 시작하는 순으로 정렬
meetings.sort(key=lambda x : (x[1], x[0]))
end_time = meetings[0][1]
result = 1
for i in range(1, n):
    if end_time <= meetings[i][0]:
        result += 1
        end_time = meetings[i][1]
print(result)