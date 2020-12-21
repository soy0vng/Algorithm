nums = list(map(int, input().split()))
while True:
    if nums == [1, 2, 3, 4, 5]:
        break
    for i in range(len(nums)-1):
        if nums[i] > nums[i+1]:
            nums[i], nums[i+1] = nums[i+1], nums[i]
            print(*nums)