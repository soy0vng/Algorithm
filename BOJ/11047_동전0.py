n, k = map(int, input().split())
coin_values = []
for _ in range(n):
    coin_values.append(int(input()))
coin_values.sort(reverse=True)

result = 0
for i in range(n):
    if k == 0:
        break
    if coin_values[i] <= k:
        result += k // coin_values[i]
        k %= coin_values[i]
print(result)