k = int(input())
result = []
for _ in range(k):
    number = int(input())
    if number != 0:
        result.append(number)
    else:
        result.pop()
print(sum(result))