n = int(input())
ropes = []
for _ in range(n):
    ropes.append(int(input()))
ropes.sort(reverse=True)
max_weight = ropes[0]
for i in range(1, n):
    max_weight = max(max_weight, ropes[i]*(i+1))
print(max_weight)
