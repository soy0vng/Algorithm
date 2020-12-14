def calc(num, idx, add, sub, mul, div):
    global max_num, min_num

    if idx == n:
        max_num = max(num, max_num)
        min_num = min(num, min_num)
        return
    else:
        if add:
            calc(num + numbers[idx], idx + 1, add - 1, sub, mul, div)
        if sub:
            calc(num - numbers[idx], idx + 1, add, sub - 1, mul, div)
        if mul:
            calc(num * numbers[idx], idx + 1, add, sub, mul - 1, div)
        if div:
            calc(int(num / numbers[idx]), idx + 1, add, sub, mul, div - 1)


n = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())
max_num = -987654321
min_num = 987654321
calc(numbers[0], 1, add, sub, mul, div)
print(max_num)
print(min_num)