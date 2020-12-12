import sys
from collections import Counter

n = int(sys.stdin.readline())
numbers = []
for _ in range(n):
    numbers.append(int(sys.stdin.readline()))


def mean(nums):
    return round(sum(nums)/len(nums))


def median(nums):
    nums.sort()
    return nums[len(nums)//2]   # n은 홀수


def mode(nums):
    modes_dict = Counter(nums)
    modes = modes_dict.most_common()

    if len(modes) == 1:
        return modes[0][0]
    else:
        if modes[0][1] == modes[1][1]:
            return modes[1][0]
        else:
            return modes[0][0]


def scope(nums):
    return max(nums) - min(nums)


print(mean(numbers))
print(median(numbers))
print(mode(numbers))
print(scope(numbers))