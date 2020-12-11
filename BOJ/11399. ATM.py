n = int(input())
waiting_time = list(map(int, input().split()))

result = 0
waiting_time.sort()
for i in range(n):
    result += sum(waiting_time[:i+1])
print(result)