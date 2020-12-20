def binary_search(numbers, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if numbers[mid] == target:
            return 1
        elif numbers[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0


n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

m = int(input())
find_list = list(map(int, input().split()))
for i in find_list:
    print(binary_search(numbers, i, 0, n-1))